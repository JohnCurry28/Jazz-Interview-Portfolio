from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field


class LifecycleState(str, Enum):
    DRAFT = "DRAFT"
    TECHNICAL_REVIEW = "TECHNICAL_REVIEW"
    CONTENT_OWNER_REVIEW = "CONTENT_OWNER_REVIEW"
    APPROVED = "APPROVED"
    PUBLISHED = "PUBLISHED"
    MONITORED = "MONITORED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    RETIRED = "RETIRED"


class CheckStatus(str, Enum):
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"


class ContentCreate(BaseModel):
    title: str = Field(min_length=3, max_length=160)
    content_type: str = Field(min_length=2, max_length=80)
    owner: str = Field(min_length=2, max_length=120)
    source_authority: str = Field(min_length=2, max_length=160)
    version: str = Field(pattern=r"^\d+\.\d+$")
    review_due_date: str
    body: str = Field(min_length=20)
    alt_text_complete: bool = True
    captions_complete: bool = True
    heading_order_valid: bool = True
    descriptive_links: bool = True
    approved_source: bool = True


class ReviewDecision(BaseModel):
    reviewer: str = Field(min_length=2, max_length=120)
    action: str = Field(pattern=r"^(APPROVE|REJECT|REQUEST_CHANGES|PUBLISH|RETIRE)$")
    note: str = Field(min_length=2, max_length=500)


class AgentScanRequest(BaseModel):
    item_id: int
    actor: str = "governance-agent"
