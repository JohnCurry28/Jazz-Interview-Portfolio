from __future__ import annotations

import uuid

from .audit import record_event
from .guardrails import detect_prompt_injection, detect_sensitive_request
from .knowledge import load_chunks, visible_to_role
from .models import Citation, CoachRequest, CoachResponse, GuardrailResult
from .retrieval import normalized_confidence, retrieve

MIN_CONFIDENCE = 0.58


def _citation_from_hit(hit) -> Citation:
    excerpt = hit.chunk.text.strip()
    if len(excerpt) > 260:
        excerpt = excerpt[:257].rstrip() + "..."
    return Citation(
        document_id=hit.chunk.document_id,
        title=hit.chunk.title,
        section=hit.chunk.section,
        excerpt=excerpt,
        source_version=hit.chunk.version,
        relevance=round(hit.score, 2),
    )


def _recommend_actions(question: str, citations: list[Citation]) -> list[str]:
    q = question.lower()
    actions: list[str] = []
    if "campaign" in q:
        actions.append("Open the campaign readiness checklist and verify every required approval before launch.")
    if "crm" in q:
        actions.append("Confirm the CRM record is complete before progressing the workflow.")
    if "manager" in q or "escalat" in q:
        actions.append("Use the defined escalation route if the issue falls outside your role authority.")
    if citations:
        actions.append("Review the cited approved source sections before taking the operational action.")
    return actions[:3]


def _synthesize(question: str, citations: list[Citation]) -> str:
    # Deterministic grounded synthesis keeps the demo fully runnable without an external model.
    # A production deployment can replace this function with an approved LLM provider while
    # preserving the same retrieval, access-control, citation, refusal, and audit contracts.
    evidence = [c.excerpt for c in citations[:3]]
    if not evidence:
        return ""
    lead = "Based only on the approved knowledge available for your role, "
    q = question.lower()
    if "campaign" in q:
        return lead + "the workflow requires readiness checks before launch. " + " ".join(evidence)
    if "crm" in q:
        return lead + "the CRM workflow should follow the documented record, validation, and escalation steps. " + " ".join(evidence)
    return lead + "here is the supported guidance: " + " ".join(evidence)


def answer_question(request: CoachRequest) -> CoachResponse:
    request_id = str(uuid.uuid4())
    reasons: list[str] = []

    if detect_prompt_injection(request.question):
        reasons.append("Prompt-injection pattern detected; retrieval and generation were not executed.")
        audit_id = record_event(
            user_id=request.user_id,
            role=request.role,
            question=request.question,
            status="blocked",
            confidence=0.0,
            grounded=False,
            citation_ids=[],
            guardrail_reasons=reasons,
        )
        return CoachResponse(
            request_id=request_id,
            status="blocked",
            answer="I can't follow instructions that attempt to bypass the assistant's security or access controls.",
            confidence=0.0,
            grounded=False,
            citations=[],
            recommended_actions=["Rephrase the question as a normal work-related request."],
            guardrails=GuardrailResult(allowed=False, reasons=reasons, prompt_injection_detected=True),
            audit_event_id=audit_id,
        )

    if detect_sensitive_request(request.question):
        reasons.append("Sensitive personal-data request is outside the scope of this performance-support demo.")
        audit_id = record_event(
            user_id=request.user_id,
            role=request.role,
            question=request.question,
            status="blocked",
            confidence=0.0,
            grounded=False,
            citation_ids=[],
            guardrail_reasons=reasons,
        )
        return CoachResponse(
            request_id=request_id,
            status="blocked",
            answer="I can't provide or retrieve sensitive personal data. Use the approved enterprise system and privacy process for that information.",
            confidence=0.0,
            grounded=False,
            citations=[],
            recommended_actions=["Use the approved privacy-safe workflow or contact the designated data owner."],
            guardrails=GuardrailResult(allowed=False, reasons=reasons),
            audit_event_id=audit_id,
        )

    all_chunks = load_chunks()
    visible, filtered_count = visible_to_role(all_chunks, request.role)
    hits = retrieve(request.question, visible)
    confidence = normalized_confidence(hits)

    if not hits or confidence < MIN_CONFIDENCE:
        reasons.append("Approved evidence did not meet the grounding threshold.")
        audit_id = record_event(
            user_id=request.user_id,
            role=request.role,
            question=request.question,
            status="refused",
            confidence=confidence,
            grounded=False,
            citation_ids=[],
            guardrail_reasons=reasons,
        )
        return CoachResponse(
            request_id=request_id,
            status="refused",
            answer="I don't have enough approved information for your role to answer that reliably. I won't guess.",
            confidence=confidence,
            grounded=False,
            citations=[],
            recommended_actions=["Search the approved knowledge repository or escalate to the appropriate content owner."],
            guardrails=GuardrailResult(
                allowed=True,
                reasons=reasons,
                access_filtered_count=filtered_count,
            ),
            audit_event_id=audit_id,
        )

    citations = [_citation_from_hit(hit) for hit in hits[:3]]
    answer = _synthesize(request.question, citations)
    audit_id = record_event(
        user_id=request.user_id,
        role=request.role,
        question=request.question,
        status="answered",
        confidence=confidence,
        grounded=True,
        citation_ids=[c.document_id for c in citations],
        guardrail_reasons=[],
    )
    return CoachResponse(
        request_id=request_id,
        status="answered",
        answer=answer,
        confidence=confidence,
        grounded=True,
        citations=citations,
        recommended_actions=_recommend_actions(request.question, citations),
        guardrails=GuardrailResult(allowed=True, access_filtered_count=filtered_count),
        audit_event_id=audit_id,
    )
