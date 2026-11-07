"""Opt-in pytest plugin: record every derivation outcome across the suite.

Run the same suite before and after a refactor and compare the two traces with
``tests/goldens/compare_traces.py``. Each entry is keyed by test node, function
and call order, so temporary paths in arguments never affect the comparison.
Outcomes are structural SHA-256 digests, with ISO timestamps masked, of packet bytes, prompts, scopes, resolved reports,
parsed artifacts or the exception type, code, stage and fixed message.

    SENTRYINSIGHT_TRACE=before.jsonl PYTHONPATH=.:tests \
        uv run --frozen pytest -q -p goldens.trace_plugin tests
"""

from __future__ import annotations

import dataclasses
import datetime
import enum
import functools
import hashlib
import json
import os
import re
import sys
from typing import Any, Callable

TARGETS = {
    "src.core.source_review": (
        "prepare_source_review",
        "plan_reporting_catalog",
        "validate_review_packet",
    ),
    "src.core.finding_evidence": (
        "build_finding_detail_context",
        "_partition_detail_spans",
        "validate_finding_evidence",
        "validate_vendor_links",
        "assess_exploitation",
    ),
    "src.core.version_references": (
        "_scopes",
        "_finding_scope",
        "validate_resolved_version_status",
        "resolve_version_references",
        "build_version_reference_context",
    ),
    "src.core.exploitation_prompt": (
        "build_exploitation_prompt",
        "estimate_prompt_tokens",
    ),
    "src.core.reviewed_report": ("resolve_reviewed_analysis",),
    "src.core.report_artifact": ("parse_report_artifact",),
}

# Reports embed their wall-clock generation time; it is not a derivation.
TIMESTAMP = re.compile(
    r"\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:?\d{2})?"
)

_state: dict[str, Any] = {"node": "<collection>", "seq": {}, "stream": None}


def _plain(value: Any) -> Any:
    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        return {
            "__type__": type(value).__name__,
            **{
                field.name: _plain(getattr(value, field.name))
                for field in dataclasses.fields(value)
            },
        }
    if isinstance(value, enum.Enum):
        return value.value
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set, frozenset)):
        items = [_plain(item) for item in value]
        return sorted(items, key=repr) if isinstance(value, (set, frozenset)) else items
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return repr(value)


def _digest(value: Any) -> str:
    """Structural SHA-256 of a value; equal values give equal digests.

    Each distinct string object is hashed once by content, so spans sharing one
    large paragraph stay linear and object identity never affects the result.
    """
    strings: dict[int, bytes] = {}

    def walk(item: Any) -> bytes:
        if isinstance(item, str):
            key = id(item)
            if key not in strings:
                text = TIMESTAMP.sub("<timestamp>", item)
                strings[key] = hashlib.sha256(b"s" + text.encode()).digest()
            return strings[key]
        if isinstance(item, datetime.datetime):
            return hashlib.sha256(b"<timestamp>").digest()
        if isinstance(item, enum.Enum):
            return hashlib.sha256(b"e" + walk(item.value)).digest()
        if dataclasses.is_dataclass(item) and not isinstance(item, type):
            parts = [type(item).__name__.encode()] + [
                walk(field.name) + walk(getattr(item, field.name))
                for field in dataclasses.fields(item)
            ]
        elif isinstance(item, dict):
            parts = [b"d"] + [walk(str(k)) + walk(v) for k, v in item.items()]
        elif isinstance(item, (list, tuple)):
            parts = [b"l" if isinstance(item, list) else b"t"]
            parts += [walk(child) for child in item]
        elif isinstance(item, (set, frozenset)):
            parts = [b"z"] + sorted(walk(child) for child in item)
        elif isinstance(item, (bool, int, float)) or item is None:
            parts = [b"v", repr(item).encode()]
        else:
            parts = [b"r", repr(item).encode()]
        return hashlib.sha256(b"\0".join(parts)).digest()

    return walk(value).hex()


def _error(exc: BaseException) -> dict[str, Any]:
    return {
        "error": type(exc).__name__,
        "code": getattr(exc, "code", None),
        "stage": getattr(exc, "stage", None),
        "field": getattr(exc, "field", None),
        "message": str(exc),
    }


def _wrap(name: str, original: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(original)
    def traced(*args: Any, **kwargs: Any) -> Any:
        node = _state["node"]
        key = (node, name)
        seq = _state["seq"][key] = _state["seq"].get(key, 0) + 1
        try:
            result = original(*args, **kwargs)
        except BaseException as exc:
            outcome: Any = _error(exc)
            _write(node, name, seq, outcome)
            raise
        _write(node, name, seq, result)
        return result

    traced.__wrapped_original__ = original  # type: ignore[attr-defined]
    return traced


def _write(node: str, name: str, seq: int, outcome: Any) -> None:
    stream = _state["stream"]
    if stream is not None:
        stream.write(
            json.dumps([node, name, seq, _digest(outcome)], ensure_ascii=True) + "\n"
        )


def _install() -> None:
    originals = {}
    for module_name, names in TARGETS.items():
        module = __import__(module_name, fromlist=["_"])
        for name in names:
            original = getattr(module, name)
            original = getattr(original, "__wrapped_original__", original)
            originals[id(original)] = (
                original,
                _wrap(f"{module_name}.{name}", original),
            )
    for module in list(sys.modules.values()):
        namespace = getattr(module, "__dict__", None)
        if not isinstance(namespace, dict):
            continue
        for attribute, value in list(namespace.items()):
            pair = originals.get(id(value)) if callable(value) else None
            if pair is not None and pair[0] is value:
                namespace[attribute] = pair[1]


def pytest_configure(config: Any) -> None:
    path = os.environ.get("SENTRYINSIGHT_TRACE")
    if path:
        _state["stream"] = open(path, "w", encoding="utf-8")


def pytest_collection_finish(session: Any) -> None:
    if _state["stream"] is not None:
        _install()


def pytest_runtest_setup(item: Any) -> None:
    _state["node"] = item.nodeid
    if _state["stream"] is not None:
        # Legacy tests reload modules; rebind any fresh references each test.
        _install()


def pytest_unconfigure(config: Any) -> None:
    if _state["stream"] is not None:
        _state["stream"].close()
        _state["stream"] = None
