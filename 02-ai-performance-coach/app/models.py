from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Literal

Role = Literal["sales_rep", "manager", "marketing", "admin"]


class CoachRequest(BaseModel):
    user_id: str = Field(min_length=1)
    role: Role
    question: str = Field(min_length=3, max_length=2000)


class Citation(BaseModel):
    document_id: str
    title: str
    section: str
    excerpt: str
    source_version: str
    relevance: float


class GuardrailResult(BaseModel):
    allowed: bool
    reasons: list[str] = []
    prompt_injection_detected: bool = False
    access_filtered_count: int = 0


class CoachResponse(BaseModel):
    request_id: str
    status: Literal["answered", "refused", "blocked"]
    answer: str
    confidence: float
    grounded: bool
    citations: list[Citation]
    recommended_actions: list[str]
    guardrails: GuardrailResult
    audit_event_id: str


class EvalCase(BaseModel):
    name: str
    role: Role
    question: str
    expected_status: Literal["answered", "refused", "blocked"]
    must_cite: bool = False
