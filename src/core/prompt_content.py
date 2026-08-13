"""Build the exact source content made visible to the analysis model."""

PROMPT_ARTICLE_CHAR_LIMIT = 2000


def get_prompt_visible_content(content: str) -> str:
    visible_content = content[:PROMPT_ARTICLE_CHAR_LIMIT]
    if len(content) > PROMPT_ARTICLE_CHAR_LIMIT:
        visible_content += "..."
    return visible_content
