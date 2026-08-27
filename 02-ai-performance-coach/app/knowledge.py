from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = BASE_DIR / "data" / "knowledge"


@dataclass(frozen=True)
class KnowledgeChunk:
    document_id: str
    title: str
    section: str
    text: str
    version: str
    allowed_roles: tuple[str, ...]
    tags: tuple[str, ...]


def load_chunks() -> list[KnowledgeChunk]:
    chunks: list[KnowledgeChunk] = []
    for path in sorted(KNOWLEDGE_DIR.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for section in payload["sections"]:
            chunks.append(
                KnowledgeChunk(
                    document_id=payload["document_id"],
                    title=payload["title"],
                    section=section["heading"],
                    text=section["text"],
                    version=payload["version"],
                    allowed_roles=tuple(payload["allowed_roles"]),
                    tags=tuple(section.get("tags", [])),
                )
            )
    return chunks


def visible_to_role(chunks: Iterable[KnowledgeChunk], role: str) -> tuple[list[KnowledgeChunk], int]:
    visible: list[KnowledgeChunk] = []
    filtered = 0
    for chunk in chunks:
        if role in chunk.allowed_roles or "all" in chunk.allowed_roles:
            visible.append(chunk)
        else:
            filtered += 1
    return visible, filtered
