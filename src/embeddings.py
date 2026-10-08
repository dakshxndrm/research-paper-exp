"""Embedding + dense retrieval.

Uses a plain NumPy cosine-similarity index rather than FAISS. At this corpus
scale (hundreds of units, ~100 queries) exhaustive search is instant, and it
removes a fragile dependency. Results are identical to FAISS flat-IP search.
"""

from __future__ import annotations

from typing import Any, Dict, List, Sequence, Tuple

import numpy as np

# sentence-transformers is imported lazily inside get_encoder(). It pulls in
# torch, which is slow to import and unnecessary for the pure-logic modules and
# unit tests that only need chunking, linking, or metric functions.
_MODEL_CACHE: Dict[str, Any] = {}


def get_encoder(model_name: str) -> Any:
    """Load (and cache) the sentence-transformer model."""
    if model_name not in _MODEL_CACHE:
        from sentence_transformers import SentenceTransformer

        _MODEL_CACHE[model_name] = SentenceTransformer(model_name)
    return _MODEL_CACHE[model_name]


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
        self.texts = list(texts)
        self.model_name = model_name
        self.batch_size = batch_size
        self.matrix = encode(self.texts, model_name, batch_size)

    def search(
        self, query: str, top_k: int, allowed_ids: Sequence[int] | None = None
    ) -> List[Tuple[int, float]]:
        """Return (index, score) pairs sorted by descending cosine similarity.

        `allowed_ids` restricts the search space -- used by the metadata
        pre-filter and the index.md routing step in the OKF arm.
        """
        q = encode([query], self.model_name, self.batch_size)[0]
        scores = self.matrix @ q

        if allowed_ids is not None:
            mask = np.full(scores.shape, -np.inf, dtype=np.float32)
            allowed = np.asarray(list(allowed_ids), dtype=int)
            if allowed.size == 0:
                return []
            mask[allowed] = scores[allowed]
            scores = mask

        k = min(top_k, int(np.isfinite(scores).sum()))
        if k <= 0:
            return []
        top = np.argpartition(-scores, k - 1)[:k]
        top = top[np.argsort(-scores[top])]
        return [(int(i), float(scores[i])) for i in top]
