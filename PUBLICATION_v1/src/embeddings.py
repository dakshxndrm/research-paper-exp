"""Embedding + dense retrieval.

Uses a plain NumPy cosine-similarity index rather than FAISS. At this corpus
scale (hundreds of units, ~100 queries) exhaustive search is instant, and it
removes a fragile dependency. Results are identical to FAISS flat-IP search.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any, List, Sequence, Tuple

import numpy as np


@lru_cache(maxsize=None)
def get_encoder(model_name: str) -> Any:
    """Load (and cache) the sentence-transformer model.

    sentence-transformers is imported lazily here. It pulls in torch, which is
    slow to import and unnecessary for the pure-logic modules and unit tests
    that only need chunking, linking, or metric functions.
    """
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(model_name)


def encode(texts: Sequence[str], model_name: str, batch_size: int = 32) -> np.ndarray:
    """Encode texts into L2-normalised embeddings, so dot product == cosine."""
    model = get_encoder(model_name)
    vectors = model.encode(
        list(texts),
        batch_size=batch_size,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    )
    return vectors.astype(np.float32)


class DenseIndex:
    """Exhaustive cosine-similarity index over a fixed set of text units."""

    def __init__(self, texts: Sequence[str], model_name: str, batch_size: int = 32):
        if not texts:
            raise ValueError("Cannot build an index over zero texts.")
        self.model_name = model_name
        self.batch_size = batch_size
        self.matrix = encode(texts, model_name, batch_size)

    def search(self, query: str, top_k: int) -> List[Tuple[int, float]]:
        """Return (index, score) pairs sorted by descending cosine similarity."""
        q = encode([query], self.model_name, self.batch_size)[0]
        scores = self.matrix @ q

        k = min(top_k, len(scores))
        if k <= 0:
            return []
        top = np.argpartition(-scores, k - 1)[:k]
        top = top[np.argsort(-scores[top])]
        return [(int(i), float(scores[i])) for i in top]
