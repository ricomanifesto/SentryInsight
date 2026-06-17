"""OpenCode-backed model client for report generation."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import httpx

DEFAULT_OPENCODE_BASE_URL = "http://127.0.0.1:4096"
OPENCODE_BASE_URL_ENV_VAR = "OPENCODE_BASE_URL"
OPENCODE_SERVER_USERNAME_ENV_VAR = "OPENCODE_SERVER_USERNAME"
OPENCODE_SERVER_PASSWORD_ENV_VAR = "OPENCODE_SERVER_PASSWORD"


class OpenCodeError(RuntimeError):
    """Raised when OpenCode cannot return usable model output."""


@dataclass(frozen=True)
class ModelSelection:
    """Provider and model IDs accepted by the OpenCode message API."""

    provider_id: str
    model_id: str

    def as_payload(self) -> dict[str, str]:
        return {"providerID": self.provider_id, "modelID": self.model_id}


def resolve_opencode_base_url() -> str:
    """Return the configured OpenCode server URL."""
    return os.getenv(OPENCODE_BASE_URL_ENV_VAR, DEFAULT_OPENCODE_BASE_URL).rstrip("/")


def parse_model_selection(model_name: str) -> ModelSelection | None:
    """Parse an explicit provider/model value."""
    model_name = model_name.strip()
    if not model_name:
        return None

    if "/" not in model_name:
        raise ValueError("Model must use provider/model format")

    provider_id, model_id = model_name.split("/", 1)
    if provider_id and model_id:
        return ModelSelection(provider_id=provider_id, model_id=model_id)
    raise ValueError("Model must use provider/model format")


class OpenCodeClient:
    """Small HTTP client for OpenCode's session message API."""

    def __init__(
        self,
        base_url: str | None = None,
        timeout: float = 120.0,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self.base_url = (base_url or resolve_opencode_base_url()).rstrip("/")
        self.timeout = timeout
        self.transport = transport

    async def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        model: ModelSelection | None = None,
        title: str = "Report generation",
    ) -> str:
        """Generate text through an OpenCode server session."""
        auth = self._auth()
        async with httpx.AsyncClient(
            base_url=self.base_url,
            timeout=self.timeout,
            transport=self.transport,
            auth=auth,
        ) as client:
            session_response = await client.post("/session", json={"title": title})
            self._raise_for_status(session_response, "create OpenCode session")
            session_id = session_response.json().get("id")
            if not session_id:
                raise OpenCodeError("OpenCode did not return a session id")

            body: dict[str, Any] = {
                "system": system_prompt,
                "parts": [{"type": "text", "text": user_prompt}],
            }
            if model is not None:
                body["model"] = model.as_payload()

            message_response = await client.post(
                f"/session/{session_id}/message",
                json=body,
            )
            self._raise_for_status(message_response, "generate OpenCode message")
            return self._extract_text(message_response.json())

    def _auth(self) -> tuple[str, str] | None:
        password = os.getenv(OPENCODE_SERVER_PASSWORD_ENV_VAR, "")
        if not password:
            return None
        username = os.getenv(OPENCODE_SERVER_USERNAME_ENV_VAR, "opencode")
        return (username, password)

    def _raise_for_status(self, response: httpx.Response, action: str) -> None:
        if response.is_success:
            return
        raise OpenCodeError(
            f"Failed to {action}: HTTP {response.status_code} {response.text}"
        )

    def _extract_text(self, payload: dict[str, Any]) -> str:
        parts = payload.get("parts", [])
        text_parts: list[str] = []
        for part in parts:
            if not isinstance(part, dict):
                continue
            text = part.get("text")
            if isinstance(text, str) and text.strip():
                text_parts.append(text)
                continue
            content = part.get("content")
            if isinstance(content, str) and content.strip():
                text_parts.append(content)

        if text_parts:
            return "\n".join(text_parts)

        info = payload.get("info", {})
        if isinstance(info, dict):
            text = info.get("text") or info.get("content")
            if isinstance(text, str) and text.strip():
                return text

        raise OpenCodeError("OpenCode response did not include text output")
