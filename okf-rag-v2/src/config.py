"""Config loading, seeding, and shared small utilities."""

from __future__ import annotations

import os
import random
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import pandas as pd
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _load_dotenv() -> None:
    """Populate os.environ from .env, without adding a dependency.

    llm.py reads credentials straight off os.environ, so before this a key
    sitting in .env was invisible to every run -- v1 only worked because the
    key happened to be exported in the shell. setdefault, not assignment: a
    real exported variable must still win over the file.
    """
    path = PROJECT_ROOT / ".env"
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        os.environ.setdefault(name.strip(), value.strip())


_load_dotenv()


def _deep_merge(base: Dict[str, Any], overlay: Dict[str, Any]) -> Dict[str, Any]:
    for key, value in overlay.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            _deep_merge(base[key], value)
        else:
            base[key] = value
    return base


def _read(cfg_path: Path) -> Dict[str, Any]:
    """Read one config, applying `extends:` so a variant only states its diff.

    A variant config that copies the whole base file drifts the moment anyone
    edits a shared value -- the ablation then runs settings nobody meant.
    """
    with open(cfg_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    parent = cfg.pop("extends", None)
    if parent is None:
        return cfg
    return _deep_merge(_read((cfg_path.parent / parent).resolve()), cfg)


def load_config(path: str | Path | None = None) -> Dict[str, Any]:
    """Load config.yaml and resolve all paths relative to the project root."""
    cfg_path = Path(path) if path else PROJECT_ROOT / "config.yaml"
    cfg = _read(cfg_path)

    for key, value in cfg["paths"].items():
        cfg["paths"][key] = str(PROJECT_ROOT / value)

    # Every LLM client gets the experiment seed unless it overrides it, so no
    # call site can silently forget to send one.
    for section in ("generation", "judge", "bundle_builder"):
        if isinstance(cfg.get(section), dict):
            cfg[section].setdefault("seed", cfg["experiment"]["seed"])

    return cfg


def set_seed(seed: int) -> None:
    """Fix seeds so a rerun reproduces the same numbers."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)


def estimate_tokens(text: str) -> int:
    """Cheap tokenizer-free token estimate (~4 chars per token).

    Deliberately approximate. It is applied identically to both arms, so the
    context budget comparison stays fair even though the absolute count is not
    exact. Document this choice in the paper's implementation details.
    """
    return max(1, len(text) // 4)


# --------------------------------------------------------------------------- #
# Incremental result writing. Shared by run_experiment and evaluate: both stream
# one paid LLM call per row, and both must resume rather than repay on a crash.
# --------------------------------------------------------------------------- #


def done_keys(path: Path, cols: List[str]) -> set:
    """Key tuples already written to a partially completed output file.

    A run is dozens of paid LLM calls; a crash or a rate-limit at question 40
    should not throw away the first 39. Keys are stringified because pandas
    reads a numeric qid back as int64 while the questions frame may hold str.
    """
    if not path.exists():
        return set()
    df = pd.read_csv(path)
    if df.empty:
        return set()
    return {tuple(str(v) for v in row) for row in df[cols].itertuples(index=False)}


def append_row(row: Dict[str, Any], path: Path) -> None:
    """Write one row immediately, so an interrupted run keeps what it paid for."""
    pd.DataFrame([row]).to_csv(path, mode="a", header=not path.exists(), index=False)
