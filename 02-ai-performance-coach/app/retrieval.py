from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass

from .knowledge import KnowledgeChunk

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "before", "by", "can", "do",
    "for", "from", "how", "i", "in", "is", "it", "my", "of", "on", "or",
    "should", "the", "to", "what", "when", "with", "you", "your"
}


@dataclass(frozen=True)
class RetrievalHit:
    chunk: KnowledgeChunk
    score: float


def tokenize(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]+", text.lower()) if t not in STOP_WORDS and len(t) > 1]


def _idf(term: str, docs: list[list[str]]) -> float:
    containing = sum(1 for doc in docs if term in doc)
    return math.log((len(docs) + 1) / (containing + 1)) + 1.0


def retrieve(question: str, chunks: list[KnowledgeChunk], top_k: int = 4) -> list[RetrievalHit]:
    if not chunks:
        return []

    query_tokens = tokenize(question)
    if not query_tokens:
        return []

    corpus = [tokenize(f"{c.title} {c.section} {' '.join(c.tags)} {c.text}") for c in chunks]
    q_counts = Counter(query_tokens)
    scored: list[RetrievalHit] = []

    for chunk, doc_tokens in zip(chunks, corpus):
        d_counts = Counter(doc_tokens)
        score = 0.0
        for term, q_tf in q_counts.items():
            if term in d_counts:
                score += (1 + math.log(q_tf)) * (1 + math.log(d_counts[term])) * _idf(term, corpus)
        q_lower = question.lower()
        text_lower = f"{chunk.section} {chunk.text}".lower()
        for phrase in ["omnichannel campaign", "crm", "manager escalation", "approved content", "data privacy", "ai use"]:
            if phrase in q_lower and phrase in text_lower:
                score += 3.0
        if score > 0:
            scored.append(RetrievalHit(chunk=chunk, score=score))

    scored.sort(key=lambda x: x.score, reverse=True)
    return scored[:top_k]


def normalized_confidence(hits: list[RetrievalHit]) -> float:
    if not hits:
        return 0.0
    top = hits[0].score
    # Bounded confidence heuristic for demo transparency; not a calibrated probability.
    return round(min(0.97, 0.40 + (top / (top + 7.0)) * 0.57), 2)
