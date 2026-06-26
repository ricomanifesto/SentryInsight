"""Validation rules for generated exploitation reports."""

from dataclasses import dataclass
import html
from html.parser import HTMLParser
import re
from typing import Iterable, List

REQUIRED_SECTIONS = (
    "# Exploitation Report",
    "## Active Exploitation Details",
    "## Affected Systems and Products",
    "## Attack Vectors and Techniques",
    "## Threat Actor Activities",
)
SOURCE_ATTRIBUTION_SECTION = "## Source Attribution"
SOURCE_ATTRIBUTION_SECTION_PATTERN = re.compile(
    rf"^{re.escape(SOURCE_ATTRIBUTION_SECTION)}\s*$",
    re.MULTILINE,
)
SOURCE_ATTRIBUTION_ENTRY_PATTERN = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)")

ERROR_MARKERS = (
    "# Error",
    "Error code:",
    "Error Generating Exploitation Report",
    "Invalid Model",
    "credit balance is too low",
    "authentication_error",
    "not_found_error",
    "rate_limit_error",
    "overloaded_error",
)

ACTIVE_CONTENT_MARKERS = (
    "<script",
    "</script",
    "<iframe",
    "<object",
    "<embed",
)

MARKDOWN_ESCAPE_PATTERN = re.compile(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~])")
MARKDOWN_LINK_DESTINATION_PATTERN = re.compile(
    r"\]\(\s*(?P<destination><[^>\n]*>|[^)\s]+)"
)
MARKDOWN_REFERENCE_DESTINATION_PATTERN = re.compile(
    r"^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*(?:\r?\n[ \t]*)?"
    r"(?P<destination><[^>\n]*>|[^\s]+)",
    re.MULTILINE,
)
HTML_EVENT_ATTRIBUTE_PATTERN = re.compile(r"^on[a-z0-9_-]+$", re.IGNORECASE)
LIST_ITEM_PATTERN = re.compile(r"^[ \t]{0,3}(?:[-+*]|\d+[.)])\s+")
HTML_BLOCK_OPEN_PATTERN = re.compile(
    r"^<(?P<tag>[A-Za-z][A-Za-z0-9:-]*)(?:\s|>|/)",
    re.IGNORECASE,
)
HTML_BLOCK_CLOSE_PATTERN = re.compile(
    r"^</(?P<tag>[A-Za-z][A-Za-z0-9:-]*)\s*>",
    re.IGNORECASE,
)
URL_ATTRIBUTE_NAMES = {
    "action",
    "formaction",
    "href",
    "src",
    "xlink:href",
}
VOID_HTML_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}
ACTIVE_CONTENT_PATTERNS = (
    re.compile(
        r"j[\x00-\x20]*a[\x00-\x20]*v[\x00-\x20]*a[\x00-\x20]*"
        r"s[\x00-\x20]*c[\x00-\x20]*r[\x00-\x20]*i[\x00-\x20]*"
        r"p[\x00-\x20]*t[\x00-\x20]*:",
        re.IGNORECASE,
    ),
)


@dataclass(frozen=True)
class ReportValidationIssue:
    code: str
    message: str


class ActiveContentHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.has_active_content = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._check_attrs(attrs)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._check_attrs(attrs)

    def _check_attrs(self, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if HTML_EVENT_ATTRIBUTE_PATTERN.match(name):
                self.has_active_content = True
                return
            if (
                value is not None
                and name.casefold() in URL_ATTRIBUTE_NAMES
                and has_javascript_scheme(value)
            ):
                self.has_active_content = True
                return


def strip_markdown_code(markdown: str) -> str:
    """Remove code regions before active-content validation."""
    without_fenced_code = strip_fenced_code_blocks(markdown)
    without_indented_code = strip_indented_code_blocks(without_fenced_code)
    return strip_inline_code_spans(without_indented_code)


def strip_fenced_code_blocks(markdown: str) -> str:
    lines = markdown.splitlines(keepends=True)
    output: list[str] = []
    index = 0
    html_block_stack: list[str] = []
    list_content_indent: int | None = None

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        line_content = line.rstrip("\r\n")
        is_blank = not line_content.strip()
        is_indented = line_content.startswith(" ") or line_content.startswith("\t")

        max_fence_indent = (
            list_content_indent + 3 if list_content_indent is not None else 3
        )
        if not html_block_stack and (
            fence := parse_fence_opener(line, max_indent=max_fence_indent)
        ):
            index += 1
            while index < len(lines) and not is_fence_closer(
                lines[index],
                fence,
                max_indent=max_fence_indent,
            ):
                index += 1
            if index < len(lines):
                index += 1
            continue

        output.append(line)
        update_html_block_stack(stripped, html_block_stack)
        if (content_indent := list_item_content_indent(line_content)) is not None:
            list_content_indent = content_indent
        elif is_blank:
            pass
        elif not is_indented:
            list_content_indent = None
        index += 1

    return "".join(output)


def parse_fence_opener(line: str, max_indent: int = 3) -> str | None:
    stripped = line.lstrip(" \t")
    if indentation_columns(line) > max_indent:
        return None

    if stripped.startswith("```"):
        fence = stripped[: len(stripped) - len(stripped.lstrip("`"))]
        info = stripped[len(fence) :].strip()
        if "`" in info:
            return None
        return fence

    if stripped.startswith("~~~"):
        return stripped[: len(stripped) - len(stripped.lstrip("~"))]

    return None


def is_fence_closer(line: str, opener: str, max_indent: int = 3) -> bool:
    stripped = line.lstrip(" \t")
    if indentation_columns(line) > max_indent:
        return False

    fence_character = opener[0]
    closing_fence = stripped[: len(stripped) - len(stripped.lstrip(fence_character))]
    if len(closing_fence) < len(opener):
        return False

    return not stripped[len(closing_fence) :].strip()


def indentation_columns(line: str) -> int:
    columns = 0
    for character in line:
        if character == " ":
            columns += 1
        elif character == "\t":
            columns += 4 - (columns % 4)
        else:
            break
    return columns


def update_html_block_stack(stripped_line: str, stack: list[str]) -> None:
    for tag_type, tag in iter_html_tags(stripped_line):
        if tag_type == "close":
            if stack and stack[-1] == tag:
                stack.pop()
        elif tag not in VOID_HTML_TAGS:
            stack.append(tag)


def iter_html_tags(markup: str) -> Iterable[tuple[str, str]]:
    index = 0

    while index < len(markup):
        character = markup[index]
        if character != "<":
            index += 1
            continue

        tag_start = index + 1
        tag_type = "open"
        if tag_start < len(markup) and markup[tag_start] == "/":
            tag_type = "close"
            tag_start += 1

        if tag_start >= len(markup) or not markup[tag_start].isalpha():
            index += 1
            continue

        tag_end = tag_start
        while tag_end < len(markup) and (
            markup[tag_end].isalnum() or markup[tag_end] in ":-"
        ):
            tag_end += 1

        tag = markup[tag_start:tag_end].casefold()
        close_index = find_html_tag_close(markup, tag_end)
        if close_index == -1:
            index += 1
            continue

        tag_body = markup[tag_end:close_index].rstrip()
        if tag_type == "open" and tag_body.endswith("/"):
            tag_type = "selfclose"

        yield tag_type, tag
        index = close_index + 1


def find_html_tag_close(markup: str, start: int) -> int:
    quote: str | None = None
    index = start

    while index < len(markup):
        character = markup[index]
        if quote is not None:
            if character == quote:
                quote = None
        elif character in ("'", '"'):
            quote = character
        elif character == ">":
            return index

        index += 1

    return -1


def visual_columns(text: str) -> int:
    columns = 0
    for character in text:
        if character == "\t":
            columns += 4 - (columns % 4)
        else:
            columns += 1

    return columns


def list_item_content_indent(line: str) -> int | None:
    match = LIST_ITEM_PATTERN.match(line)
    if match is None:
        return None

    return visual_columns(line[: match.end()])


def strip_indented_code_blocks(markdown: str) -> str:
    lines = markdown.splitlines(keepends=True)
    output: list[str] = []
    previous_blank = True
    in_code_block = False
    list_content_indent: int | None = None
    html_block_stack: list[str] = []

    for line in lines:
        line_content = line.rstrip("\r\n")
        stripped = line_content.strip()
        is_blank = not line_content.strip()
        is_indented = line_content.startswith("    ") or line_content.startswith("\t")
        line_indent = indentation_columns(line_content)

        if html_block_stack:
            output.append(line)
            update_html_block_stack(stripped, html_block_stack)
            previous_blank = False
            in_code_block = False
            continue

        if (
            is_indented
            and list_content_indent is not None
            and line_indent >= list_content_indent + 4
            and (previous_blank or in_code_block)
        ):
            in_code_block = True
            previous_blank = False
            continue

        if is_indented and list_content_indent is not None:
            output.append(line)
            previous_blank = False
            in_code_block = False
            continue

        if is_indented and (previous_blank or in_code_block):
            in_code_block = True
            previous_blank = False
            continue

        if starts_html_block(stripped):
            output.append(line)
            update_html_block_stack(stripped, html_block_stack)
            previous_blank = False
            in_code_block = False
            continue

        if is_blank:
            output.append(line)
            previous_blank = True
            continue

        output.append(line)
        previous_blank = False
        in_code_block = False
        list_content_indent = list_item_content_indent(line_content)

    return "".join(output)


def strip_inline_code_spans(markdown: str) -> str:
    lines = markdown.splitlines(keepends=True)
    output: list[str] = []
    html_block_stack: list[str] = []

    for line in lines:
        stripped = line.strip()
        if html_block_stack or starts_html_block(stripped):
            output.append(line)
            update_html_block_stack(stripped, html_block_stack)
            continue

        output.append(strip_inline_code_spans_in_text(line))

    return "".join(output)


def strip_inline_code_spans_in_text(markdown: str) -> str:
    output: list[str] = []
    index = 0
    inside_html_tag = False
    html_quote: str | None = None

    def starts_html_tag(position: int) -> bool:
        if position + 1 >= len(markdown):
            return False

        next_character = markdown[position + 1]
        return next_character.isalpha() or next_character in "/!?"

    def append_and_track_html(characters: str, source_index: int | None = None) -> None:
        nonlocal inside_html_tag, html_quote
        for offset, character in enumerate(characters):
            output.append(character)
            if inside_html_tag:
                if html_quote:
                    if character == html_quote:
                        html_quote = None
                elif character in ('"', "'"):
                    html_quote = character
                elif character == ">":
                    inside_html_tag = False
            elif (
                character == "<"
                and source_index is not None
                and starts_html_tag(source_index + offset)
            ):
                inside_html_tag = True

    def is_escaped(position: int) -> bool:
        backslash_count = 0
        cursor = position - 1
        while cursor >= 0 and markdown[cursor] == "\\":
            backslash_count += 1
            cursor -= 1
        return bool(backslash_count % 2)

    def find_closing_delimiter(delimiter: str, start: int) -> int:
        search_index = start
        while True:
            candidate = markdown.find(delimiter, search_index)
            if candidate == -1:
                return -1

            previous_is_backtick = candidate > 0 and markdown[candidate - 1] == "`"
            next_index = candidate + len(delimiter)
            next_is_backtick = (
                next_index < len(markdown) and markdown[next_index] == "`"
            )
            if (
                not previous_is_backtick
                and not next_is_backtick
                and not is_escaped(candidate)
            ):
                return candidate

            search_index = candidate + 1

    def is_fence_like_opener(position: int, delimiter_length: int) -> bool:
        if delimiter_length < 3:
            return False

        line_start = markdown.rfind("\n", 0, position) + 1
        prefix = markdown[line_start:position]
        return len(prefix) <= 3 and prefix.strip(" \t") == ""

    while index < len(markdown):
        if markdown[index] != "`" or inside_html_tag or is_escaped(index):
            append_and_track_html(markdown[index], index)
            index += 1
            continue

        delimiter_length = 1
        while (
            index + delimiter_length < len(markdown)
            and markdown[index + delimiter_length] == "`"
        ):
            delimiter_length += 1

        if is_fence_like_opener(index, delimiter_length):
            append_and_track_html("`" * delimiter_length, index)
            index += delimiter_length
            continue

        delimiter = "`" * delimiter_length
        closing_index = find_closing_delimiter(delimiter, index + delimiter_length)
        if closing_index == -1:
            append_and_track_html(delimiter, index)
            index += delimiter_length
            continue

        index = closing_index + delimiter_length

    return "".join(output)


def normalize_markdown_escapes(markdown: str) -> str:
    """Resolve Markdown punctuation escapes before rendered-content checks."""
    return MARKDOWN_ESCAPE_PATTERN.sub(r"\1", markdown)


def preserve_markdown_escaped_html(markdown: str) -> str:
    lines = markdown.splitlines(keepends=True)
    output: list[str] = []
    html_block_stack: list[str] = []

    for line in lines:
        stripped = line.strip()
        if html_block_stack or starts_html_block(stripped):
            output.append(line)
            update_html_block_stack(stripped, html_block_stack)
        else:
            output.append(preserve_markdown_escaped_html_in_text(line))

    return "".join(output)


def preserve_markdown_escaped_html_in_text(markdown: str) -> str:
    output: list[str] = []
    for index, character in enumerate(markdown):
        if character in "<>" and has_odd_backslash_escape(markdown, index):
            if output and output[-1] == "\\":
                output.pop()
            output.append("&lt;" if character == "<" else "&gt;")
        else:
            output.append(character)

    return "".join(output)


def has_odd_backslash_escape(markdown: str, position: int) -> bool:
    backslash_count = 0
    cursor = position - 1
    while cursor >= 0 and markdown[cursor] == "\\":
        backslash_count += 1
        cursor -= 1

    return bool(backslash_count % 2)


def has_javascript_scheme(value: str) -> bool:
    return any(pattern.search(value) for pattern in ACTIVE_CONTENT_PATTERNS)


def starts_html_block(stripped_line: str) -> bool:
    return bool(
        HTML_BLOCK_OPEN_PATTERN.match(stripped_line)
        or HTML_BLOCK_CLOSE_PATTERN.match(stripped_line)
    )


def contains_active_html(markup: str) -> bool:
    parser = ActiveContentHTMLParser()
    parser.feed(markup)
    parser.close()
    return parser.has_active_content


def contains_active_markdown_link(markdown: str) -> bool:
    matches = (
        *MARKDOWN_LINK_DESTINATION_PATTERN.finditer(markdown),
        *MARKDOWN_REFERENCE_DESTINATION_PATTERN.finditer(markdown),
    )
    for match in matches:
        destination = match.group("destination")
        if destination.startswith("<") and destination.endswith(">"):
            destination = destination[1:-1]
        if has_javascript_scheme(html.unescape(destination)):
            return True

    return False


def get_source_attribution_section_body(markdown: str) -> str:
    searchable_markdown = strip_markdown_code(markdown)
    section_match = SOURCE_ATTRIBUTION_SECTION_PATTERN.search(searchable_markdown)
    if not section_match:
        return ""

    section_body_start = section_match.end()
    next_section = re.search(
        r"^##\s+", searchable_markdown[section_body_start:], re.MULTILINE
    )
    return (
        searchable_markdown[
            section_body_start : section_body_start + next_section.start()
        ]
        if next_section
        else searchable_markdown[section_body_start:]
    )


def remove_source_attribution_section(markdown: str) -> str:
    lines = markdown.splitlines(keepends=True)
    retained_lines: list[str] = []
    fence: str | None = None
    skipping_section = False

    for line in lines:
        if fence is not None:
            if is_fence_closer(line, fence):
                fence = None
            if not skipping_section:
                retained_lines.append(line)
            continue

        if fence_opener := parse_fence_opener(line):
            fence = fence_opener
            if not skipping_section:
                retained_lines.append(line)
            continue

        if SOURCE_ATTRIBUTION_SECTION_PATTERN.match(line):
            skipping_section = True
            continue

        if skipping_section and re.match(r"^##\s+", line):
            skipping_section = False

        if not skipping_section:
            retained_lines.append(line)

    return "".join(retained_lines).rstrip()


def render_source_attribution_section(source_attribution_entries: Iterable[str]) -> str:
    entries: list[str] = []
    seen_entries: set[str] = set()
    for entry in source_attribution_entries:
        cleaned_entry = entry.strip()
        if not cleaned_entry or cleaned_entry in seen_entries:
            continue
        entries.append(cleaned_entry)
        seen_entries.add(cleaned_entry)

    if not entries:
        return ""
    return f"{SOURCE_ATTRIBUTION_SECTION}\n\n" + "\n".join(entries) + "\n"


def ensure_source_attribution_section(
    markdown: str, source_attribution_entries: Iterable[str]
) -> str:
    section = render_source_attribution_section(source_attribution_entries)
    if not section:
        return markdown

    report_without_source_attribution = remove_source_attribution_section(markdown)
    return f"{report_without_source_attribution.rstrip()}\n\n{section}"


def get_source_attribution_entries(markdown: str) -> list[str]:
    section_body = get_source_attribution_section_body(markdown)
    entries: list[str] = []
    current_entry: list[str] = []

    for line in section_body.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            continue

        if SOURCE_ATTRIBUTION_ENTRY_PATTERN.match(line):
            if current_entry:
                entries.append(" ".join(current_entry))
            current_entry = [stripped_line]
            continue

        if current_entry:
            current_entry.append(stripped_line)
        else:
            entries.append(stripped_line)

    if current_entry:
        entries.append(" ".join(current_entry))

    return entries


def exact_source_attribution_entries_present(
    markdown: str, source_attribution_entries: Iterable[str]
) -> bool:
    expected_entries = {
        html.unescape(entry.strip())
        for entry in source_attribution_entries
        if entry.strip()
    }
    actual_entries = {
        html.unescape(entry) for entry in get_source_attribution_entries(markdown)
    }
    return bool(expected_entries) and expected_entries.issubset(actual_entries)


def validate_report_content(
    markdown: str,
    require_source_attribution: bool = False,
    source_attribution_entries: Iterable[str] | None = None,
) -> List[ReportValidationIssue]:
    """Return validation issues that should block publishing."""
    issues: List[ReportValidationIssue] = []
    content = markdown.strip()

    if not content:
        return [
            ReportValidationIssue(
                code="empty_report",
                message="Report is empty.",
            )
        ]

    active_content = strip_markdown_code(content)
    html_active_content = preserve_markdown_escaped_html(active_content)
    rendered_like_content = normalize_markdown_escapes(active_content)
    normalized_report_content = content.casefold()
    normalized_content = html_active_content.casefold()
    for marker in ERROR_MARKERS:
        if marker.casefold() in normalized_report_content:
            issues.append(
                ReportValidationIssue(
                    code="error_marker",
                    message=f"Report contains blocked error marker: {marker}",
                )
            )

    for marker in ACTIVE_CONTENT_MARKERS:
        if marker.casefold() in normalized_content:
            issues.append(
                ReportValidationIssue(
                    code="active_content",
                    message=f"Report contains blocked active content marker: {marker}",
                )
            )

    if contains_active_html(html_active_content):
        issues.append(
            ReportValidationIssue(
                code="active_content",
                message="Report contains blocked active HTML event handler.",
            )
        )

    has_active_markdown_link = contains_active_markdown_link(rendered_like_content)
    for pattern in ACTIVE_CONTENT_PATTERNS:
        if pattern.search(active_content) or pattern.search(rendered_like_content):
            issues.append(
                ReportValidationIssue(
                    code="active_content",
                    message="Report contains blocked JavaScript URL.",
                )
            )

    if has_active_markdown_link:
        issues.append(
            ReportValidationIssue(
                code="active_content",
                message="Report contains blocked JavaScript URL.",
            )
        )

    for section in REQUIRED_SECTIONS:
        if section not in content:
            issues.append(
                ReportValidationIssue(
                    code="missing_section",
                    message=f"Report is missing required section: {section}",
                )
            )

    source_attribution_is_valid = (
        exact_source_attribution_entries_present(content, source_attribution_entries)
        if source_attribution_entries is not None
        else False
    )
    if require_source_attribution and not source_attribution_is_valid:
        issues.append(
            ReportValidationIssue(
                code="missing_source_attribution",
                message=(
                    "Report is missing required source attribution entries in section: "
                    f"{SOURCE_ATTRIBUTION_SECTION}"
                ),
            )
        )

    return issues


def format_report_validation_issues(
    issues: Iterable[ReportValidationIssue],
) -> str:
    """Format validation issues for logs and CLI output."""
    return "\n".join(f"- {issue.code}: {issue.message}" for issue in issues)
