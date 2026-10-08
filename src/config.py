"""Config loading, seeding, and shared small utilities."""

from __future__ import annotations

import os
import random
from pathlib import Path
from typing import Any, Dict

import numpy as np
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_config(path: str | Path | None = None) -> Dict[str, Any]:
    """Load config.yaml and resolve all paths relative to the project root."""
    cfg_path = Path(path) if path else PROJECT_ROOT / "config.yaml"
    with open(cfg_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    for key, value in cfg["paths"].items():
        cfg["paths"][key] = str(PROJECT_ROOT / value)

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


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p
