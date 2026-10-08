"""Arm A -- baseline naive chunk RAG.

Fixed-size overlapping chunks over the RAW documents, dense retrieval, top-k,
truncate to the shared context budget. This is the standard pipeline the paper
argues against, so it must be implemented fairly -- no deliberate crippling.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from src.config import estimate_tokens
from src.embeddings import DenseIndex


def chunk_text(text: str, size_tokens: int, overlap_tokens: int, source: str) -> List[Dict]:
    """Split text into overlapping windows measured in approximate tokens."""
    words = text.split()
    # ~0.75 words per token for English; convert the token budget into words.
    size_w = max(1, int(size_tokens * 0.75))
    step_w = max(1, size_w - int(overlap_tokens * 0.75))

    chunks: List[Dict] = []
    for start in range(0, len(words), step_w):
        window = words[start : start + size_w]
        if not window:
            break
        chunks.append(
            {
                "id": f"{source}#chunk{len(chunks)}",
                "source": source,
                "text": " ".join(window),
            }
        )
        if start + size_w >= len(words):
            break
    return chunks


class ChunkRAG:
    """Baseline retriever. Call .retrieve(question) -> assembled context + trace."""

    def __init__(self, cfg: Dict[str, Any]):
        rc = cfg["retrieval"]["chunk"]
        self.top_k = rc["top_k"]
        self.budget = cfg["retrieval"]["context_token_budget"]

        raw_dir = Path(cfg["paths"]["raw_docs"])
        self.chunks: List[Dict] = []
        for path in sorted(raw_dir.rglob("*")):
            if path.suffix.lower() not in {".md", ".txt"} or not path.is_file():
                continue
            self.chunks.extend(
                chunk_text(
                    path.read_text(encoding="utf-8", errors="ignore"),
                    rc["chunk_size_tokens"],
                    rc["chunk_overlap_tokens"],
                    path.name,
                )
            )

        if not self.chunks:
            raise SystemExit("No chunks built -- is data/raw/ empty?")

        self.index = DenseIndex(
            [c["text"] for c in self.chunks],
            cfg["embedding"]["model"],
            cfg["embedding"]["batch_size"],
        )

    def retrieve(self, question: str) -> Dict[str, Any]:
        hits = self.index.search(question, self.top_k)

        blocks: List[str] = []
        used: List[str] = []
        spent = 0
        for idx, _ in hits:
            chunk = self.chunks[idx]
            block = f"[{chunk['id']}]\n{chunk['text']}"
            cost = estimate_tokens(block)
            if spent + cost > self.budget:
                continue
            blocks.append(block)
            used.append(chunk["id"])
            spent += cost

        return {
            "context": "\n\n---\n\n".join(blocks),
            "retrieved_ids": used,
            "n_units": len(used),
            "context_tokens": spent,
        }

    @property
    def unit_count(self) -> int:
        return len(self.chunks)
