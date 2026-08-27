from __future__ import annotations

import re

INJECTION_PATTERNS = [
    r"ignore (all|any|the|previous) instructions",
    r"reveal (the )?(system|developer) prompt",
    r"show me your hidden",
    r"bypass (security|policy|access)",
    r"act as if you are (an )?admin",
    r"disable (your )?(guardrails|safety)",
]

PROHIBITED_PERSONAL_DATA = [
    "social security number",
    "ssn",
    "patient record",
    "medical record number",
]


def detect_prompt_injection(question: str) -> bool:
    q = question.lower()
    return any(re.search(pattern, q) for pattern in INJECTION_PATTERNS)


def detect_sensitive_request(question: str) -> bool:
    q = question.lower()
    return any(term in q for term in PROHIBITED_PERSONAL_DATA)
