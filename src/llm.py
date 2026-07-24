"""Unified LLM client.

Supports three providers so the experiment can run on whatever the machine has:
  - ollama            : fully local, free, no API key  (recommended default)
  - gemini            : Google AI Studio free tier
  - openai_compatible : OpenAI, Groq, Together, vLLM, LM Studio, etc.

All providers expose the same .generate(system, user) -> str interface, so
swapping the generator model does not change any pipeline code.
"""

from __future__ import annotations

import json
import os
import re
import time
from typing import Any, Dict

import requests


class LLMError(RuntimeError):
    pass


class LLMClient:
    def __init__(self, cfg: Dict[str, Any]):
        self.provider = cfg["provider"]
        self.model = cfg["model"]
        self.temperature = cfg.get("temperature", 0.0)
        self.max_tokens = cfg.get("max_tokens", 400)
        self.timeout = cfg.get("timeout_s", 180)
        self.base_url = cfg.get("base_url", "http://localhost:11434").rstrip("/")
        self.api_key = os.environ.get(cfg.get("api_key_env", "LLM_API_KEY"), "")

        if self.provider in ("gemini", "openai_compatible") and not self.api_key:
            raise LLMError(
                f"Provider '{self.provider}' needs an API key. "
                f"Set the env var '{cfg.get('api_key_env', 'LLM_API_KEY')}'."
            )

    # ------------------------------------------------------------------ #

    def generate(self, system: str, user: str, retries: int = 3) -> str:
        """Generate a completion. Retries on transient network errors."""
        last_err: Exception | None = None
        for attempt in range(retries):
            try:
                if self.provider == "ollama":
                    return self._ollama(system, user)
                if self.provider == "gemini":
                    return self._gemini(system, user)
                if self.provider == "openai_compatible":
                    return self._openai(system, user)
                raise LLMError(f"Unknown provider: {self.provider}")
            except (requests.RequestException, LLMError) as exc:
                last_err = exc
                time.sleep(2 ** attempt)
        raise LLMError(f"LLM call failed after {retries} attempts: {last_err}")

    # ------------------------------------------------------------------ #

    def _ollama(self, system: str, user: str) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "stream": False,
            "options": {
                "temperature": self.temperature,
                "num_predict": self.max_tokens,
            },
        }
        r = requests.post(
            f"{self.base_url}/api/chat", json=payload, timeout=self.timeout
        )
        r.raise_for_status()
        return r.json()["message"]["content"].strip()

    def _gemini(self, system: str, user: str) -> str:
        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"{self.model}:generateContent?key={self.api_key}"
        )
        payload = {
            "systemInstruction": {"parts": [{"text": system}]},
            "contents": [{"role": "user", "parts": [{"text": user}]}],
            "generationConfig": {
                "temperature": self.temperature,
                "maxOutputTokens": self.max_tokens,
            },
        }
        r = requests.post(url, json=payload, timeout=self.timeout)
        r.raise_for_status()
        data = r.json()
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"].strip()
        except (KeyError, IndexError) as exc:
            raise LLMError(f"Unexpected Gemini response: {json.dumps(data)[:400]}") from exc

    def _openai(self, system: str, user: str) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }
        r = requests.post(
            f"{self.base_url}/v1/chat/completions",
            json=payload,
            headers={"Authorization": f"Bearer {self.api_key}"},
            timeout=self.timeout,
        )
        r.raise_for_status()
        choice = r.json()["choices"][0]
        content = (choice["message"].get("content") or "").strip()
        if not content:
            # Reasoning models (gpt-oss, o-series) spend max_tokens on hidden
            # reasoning first. A truncated one returns empty content, which would
            # otherwise be silently recorded as an empty answer and scored as a
            # legitimate miss. Fail loudly instead of corrupting the numbers.
            raise LLMError(
                f"Empty completion from {self.model} "
                f"(finish_reason={choice.get('finish_reason')}). "
                f"max_tokens={self.max_tokens} is likely too small -- a reasoning "
                f"model consumed the whole budget before emitting an answer."
            )
        return content


def _repair_bold_keys(text: str) -> str:
    """`**description**: "..."` -> `"description": "..."`.

    Observed from gpt-oss: it occasionally markdown-bolds one key mid-array,
    which invalidates the whole response and would cost the entire document.
    """
    return re.sub(r"\*\*(\w+)\*\*(\s*:)", r'"\1"\2', text)


def _salvage_array(text: str) -> str | None:
    """Rebuild a JSON array from its complete objects, discarding a partial tail.

    Guards the silent total-loss case: a long extraction that hits max_tokens is
    cut mid-object, so there is no closing `]` and a naive last-`]` search lands
    inside a nested "tags" array. Rather than drop the document entirely, keep
    the objects that did finish. Also handles trailing prose after the array.
    """
    start = text.find("[")
    if start == -1:
        return None

    depth = 0
    in_string = False
    escaped = False
    last_complete: int | None = None

    for i in range(start + 1, len(text)):
        ch = text[i]
        if escaped:
            escaped = False
        elif ch == "\\":
            escaped = True
        elif ch == '"':
            in_string = not in_string
        elif in_string:
            continue
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                last_complete = i

    if last_complete is None:
        return None
    return text[start : last_complete + 1] + "]"


def extract_json(text: str) -> Any:
    """Pull a JSON object/array out of an LLM response that may have prose or fences."""
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("```")[1]
        if cleaned.lstrip().lower().startswith("json"):
            cleaned = cleaned.lstrip()[4:]
    cleaned = cleaned.strip()

    repaired = _repair_bold_keys(cleaned)

    def _span(opener: str, closer: str) -> Any:
        for source in (cleaned, repaired):
            start = source.find(opener)
            end = source.rfind(closer)
            if start != -1 and end > start:
                try:
                    return json.loads(source[start : end + 1])
                except json.JSONDecodeError:
                    continue
        return None

    def _salvaged() -> Any:
        text_ = _salvage_array(repaired)
        if text_ is None:
            return None
        try:
            return json.loads(text_)
        except json.JSONDecodeError:
            return None

    # Try whichever bracket opens first. An object whose body or tags contain a
    # literal "[" would otherwise be parsed as that inner array; a truncated
    # array would be parsed as its first complete object.
    first_array = cleaned.find("[")
    first_object = cleaned.find("{")
    array_first = first_array != -1 and (first_object == -1 or first_array < first_object)

    attempts = (
        (lambda: _span("[", "]"), _salvaged, lambda: _span("{", "}"))
        if array_first
        else (lambda: _span("{", "}"), lambda: _span("[", "]"), _salvaged)
    )
    for attempt in attempts:
        result = attempt()
        if result is not None:
            return result

    raise LLMError(f"Could not parse JSON from response: {text[:300]}")
