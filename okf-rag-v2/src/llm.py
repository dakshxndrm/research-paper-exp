"""LLM client for OpenAI-compatible chat endpoints.

Covers OpenAI, Groq, Together, vLLM, LM Studio, and anything else speaking
/v1/chat/completions -- point `base_url` at it. `.generate(system, user) -> str`
is the whole interface, so swapping the model does not change pipeline code.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from typing import Any, Dict

import requests


class LLMError(RuntimeError):
    pass


class LLMClient:
    def __init__(self, cfg: Dict[str, Any]):
        self.model = cfg["model"]
        self.temperature = cfg.get("temperature", 0.0)
        self.max_tokens = cfg.get("max_tokens", 400)
        self.timeout = cfg.get("timeout_s", 180)
        self.retries = cfg.get("retries", 3)
        self.max_retry_after = cfg.get("max_retry_after_s", 120)
        self.base_url = cfg.get("base_url", "").rstrip("/")
        # Everyone speaks /v1/chat/completions except Google, whose
        # OpenAI-compatibility layer hangs it off /v1beta/openai/. One config
        # key is the whole difference -- Gemini needs no provider branch.
        self.chat_path = cfg.get("chat_path", "/v1/chat/completions")
        # api_key_env: null means a local provider (Ollama, LM Studio, vLLM) that
        # needs no credential. Anything else must actually have its key present.
        key_env = cfg.get("api_key_env", "LLM_API_KEY")
        self.api_key = os.environ.get(key_env, "") if key_env else ""
        if self.api_key:
            auth = f"key from {key_env}"
        elif key_env:
            auth = f"MISSING ({key_env} not set)"   # about to raise below
        else:
            auth = "none (local provider)"
        print(f"Endpoint: {self.base_url}{self.chat_path} | model: {self.model} | auth: {auth}")
        # config.py injects the experiment seed into every LLM section, but
        # Google's OpenAI layer hard-rejects an unknown `seed` field with a 400.
        # send_seed=false drops it for those providers.
        self.seed = cfg.get("seed") if cfg.get("send_seed", True) else None
        # Optional, off by default (None -> omitted from the payload, so this is a
        # no-op for every config that doesn't set it). Ollama's OpenAI-compatible
        # endpoint honours a top-level "reasoning_effort" for thinking models
        # ("none"/"low"/"medium"/"high"/"max"). Added 2026-08-28: bundle_builder's
        # Nemotron extraction burned its entire 16000-token budget on hidden
        # reasoning and returned an EMPTY completion on 8/8 retries for the very
        # first document -- not a budget shortfall, a runaway chain-of-thought on
        # a structured-extraction task that doesn't need deep reasoning.
        self.reasoning_effort = cfg.get("reasoning_effort")

        if key_env and not self.api_key:
            raise LLMError(f"No API key. Set the env var '{key_env}'.")

    # ------------------------------------------------------------------ #

    def generate(self, system: str, user: str) -> str:
        """Generate a completion. Retries on transient network errors."""
        retries = self.retries
        last_err: Exception | None = None
        for attempt in range(retries):
            try:
                return self._openai(system, user)
            except (requests.RequestException, LLMError) as exc:
                last_err = exc
                response = getattr(exc, "response", None)
                status = getattr(response, "status_code", None)

                if status == 429:
                    # Rate limits are per-minute windows; 1/2/4s of exponential
                    # backoff never clears one. Honour the server's own hint.
                    delay = float(response.headers.get("retry-after", 20))
                    if delay > self.max_retry_after:
                        # A per-MINUTE 429 asks for <=60s. A retry-after of many
                        # minutes means a per-day/per-hour quota is gone, and no
                        # retry loop should sit on it -- that is the "silent
                        # hang" this looked like. Fail with the body, which names
                        # the limit that was actually hit.
                        raise LLMError(
                            f"429 from {self.model}: retry-after {delay:.0f}s "
                            f"exceeds max_retry_after_s={self.max_retry_after}. "
                            f"This is a long-window quota, not a per-minute "
                            f"burst. Server said: {response.text[:300]}"
                        ) from exc
                elif status is not None and 400 <= status < 500:
                    # Deterministic client error (bad model name, payload too
                    # large). Retrying changes nothing -- fail now with the body,
                    # which carries the actual reason.
                    raise LLMError(
                        f"{status} from {self.model}: {response.text[:300]}"
                    ) from exc
                else:
                    delay = 2 ** attempt

                if attempt < retries - 1:
                    # Silent sleeps are indistinguishable from a hang. Say what
                    # we are waiting for, on stderr so tqdm does not eat it.
                    print(f"    [retry {attempt + 1}/{retries - 1}] "
                          f"status={status} err={type(exc).__name__} "
                          f"sleeping {delay:.0f}s", file=sys.stderr, flush=True)
                    time.sleep(delay)
        raise LLMError(f"LLM call failed after {retries} attempts: {last_err}")

    # ------------------------------------------------------------------ #

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
        if self.reasoning_effort is not None:
            payload["reasoning_effort"] = self.reasoning_effort
        if self.seed is not None:
            # Best-effort only. Groq accepts `seed`, but on a mixture-of-experts
            # model it reduces drift rather than guaranteeing identical output:
            # expert routing still varies with batching on the server side. Do
            # not describe runs as bit-reproducible in the paper on this basis.
            payload["seed"] = self.seed
        r = requests.post(
            f"{self.base_url}{self.chat_path}",
            json=payload,
            headers={"Authorization": f"Bearer {self.api_key}"} if self.api_key else {},
            timeout=self.timeout,
        )
        r.raise_for_status()
        body = r.json()
        choice = body["choices"][0]
        # Kept for calibrating max_tokens against a reasoning model: the answer
        # text alone cannot show how much of the budget hidden reasoning ate.
        # Last call only -- nothing in the pipeline reads it, it exists so a
        # smoke test can report real usage instead of guessing.
        self.last_usage = {**body.get("usage", {}),
                           "finish_reason": choice.get("finish_reason")}
        content = (choice["message"].get("content") or "").strip()
        # Reasoning models emit <think>...</think> before the answer. Ollama's
        # OpenAI-compatible endpoint does not reliably split that into a separate
        # field, and an unstripped think block corrupts EM/F1 and citation
        # parsing. rsplit, not a regex: a truncated response can carry the
        # closing tag without the opening one. No-op for a non-reasoning model
        # like v1's llama3.1:8b, so v1 reruns are byte-identical.
        if "</think>" in content:
            content = content.rsplit("</think>", 1)[1].strip()
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


def _trim_to_outermost(text: str) -> str | None:
    """Slice from the first bracket to the last of its own kind, dropping prose.

    Picks whichever of `[` / `{` opens first, so an object whose body or tags
    contain a literal "[" is not mistaken for that inner array.
    """
    opens = [(text.find(o), o, c) for o, c in (("[", "]"), ("{", "}")) if o in text]
    if not opens:
        return None
    start, _, closer = min(opens)
    end = text.rfind(closer)
    return text[start : end + 1] if end > start else None


def extract_json(text: str) -> Any:
    """Pull a JSON object/array out of an LLM response that may have prose or fences."""
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("```")[1]
        if cleaned.lstrip().lower().startswith("json"):
            cleaned = cleaned.lstrip()[4:]
    cleaned = cleaned.strip()

    # Cheapest first: a clean response parses as-is. Then strip surrounding
    # prose. Only then salvage, which discards a truncated tail and so must
    # never win over a parse that keeps everything.
    for source in (cleaned, _repair_bold_keys(cleaned)):
        for candidate in (source, _trim_to_outermost(source), _salvage_array(source)):
            if candidate is None:
                continue
            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                continue

    raise LLMError(f"Could not parse JSON from response: {text[:300]}")
