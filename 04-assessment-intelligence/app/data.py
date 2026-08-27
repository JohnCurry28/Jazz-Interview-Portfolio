from __future__ import annotations

import math
import random

CAPABILITIES = [
    "CRM Workflow",
    "Omnichannel Execution",
    "Data Literacy",
    "Responsible AI Use",
]

ROLES = [
    ("Commercial Representative", "CRM Workflow"),
    ("Marketing Manager", "Omnichannel Execution"),
    ("Commercial Analytics Partner", "Data Literacy"),
    ("Capability Manager", "Responsible AI Use"),
]

ITEM_BLUEPRINT = [
    ("Q01", "CRM Workflow", 0.10, "Record required customer-interaction information before advancing the workflow."),
    ("Q02", "CRM Workflow", -0.15, "Identify the correct CRM workflow state after a completed interaction."),
    ("Q03", "CRM Workflow", 0.35, "Select the required data-quality check before closing the record."),
    ("Q04", "Omnichannel Execution", 0.05, "Choose the appropriate sequencing principle for an omnichannel campaign."),
    ("Q05", "Omnichannel Execution", 0.30, "Recognize the approval checkpoint that must occur before activation."),
    ("Q06", "Omnichannel Execution", 0.55, "Interpret a channel-performance signal and choose the next action."),
    ("Q07", "Data Literacy", 0.00, "Distinguish a descriptive metric from an actionable capability indicator."),
    ("Q08", "Data Literacy", 0.40, "Interpret a cohort trend without confusing correlation with causation."),
    ("Q09", "Data Literacy", 0.10, "Select the best evidence for evaluating adoption after training."),
    ("Q10", "Responsible AI Use", 0.15, "Identify when an AI response requires source verification before use."),
    ("Q11", "Responsible AI Use", 0.45, "Choose the safest response when approved evidence is insufficient."),
    ("Q12", "Responsible AI Use", 0.20, "Recognize an attempt to override enterprise AI instructions."),
]


def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def build_dataset(seed: int = 20260826) -> tuple[list[dict], list[dict], list[dict]]:
    rng = random.Random(seed)
    items = [
        {
            "item_id": iid,
            "capability": capability,
            "difficulty_parameter": diff,
            "question": question,
        }
        for iid, capability, diff, question in ITEM_BLUEPRINT
    ]

    learners: list[dict] = []
    responses: list[dict] = []
    learner_count = 96
    for i in range(learner_count):
        role, primary_cap = ROLES[i % len(ROLES)]
        ability = rng.gauss(0.55, 0.75)
        completion = min(1.0, max(0.70, rng.gauss(0.965, 0.035)))

        base_adoption = sigmoid((ability - 0.10) * 1.3)
        role_drag = {
            "Commercial Representative": 0.08,
            "Marketing Manager": 0.18,
            "Commercial Analytics Partner": 0.10,
            "Capability Manager": 0.06,
        }[role]
        adoption = min(0.98, max(0.25, base_adoption - role_drag + rng.gauss(0, 0.08)))
        business = min(0.98, max(0.25, 0.40 + 0.46 * adoption + 0.10 * sigmoid(ability) + rng.gauss(0, 0.06)))

        learner = {
            "learner_id": f"EMP-{i+1:03d}",
            "role": role,
            "primary_capability": primary_cap,
            "completion_score": round(completion, 4),
            "adoption_score": round(adoption, 4),
            "business_outcome_score": round(business, 4),
        }
        learners.append(learner)

        for iid, capability, item_diff, _ in ITEM_BLUEPRINT:
            cap_bonus = 0.18 if capability == primary_cap else 0.0
            if iid == "Q09":
                p_correct = sigmoid((-ability - item_diff) * 1.35)
            elif iid == "Q06":
                p_correct = sigmoid((ability + cap_bonus - item_diff - 0.35) * 1.35)
            else:
                p_correct = sigmoid((ability + cap_bonus - item_diff + 0.45) * 1.35)
            correct = 1 if rng.random() < p_correct else 0
            responses.append({"learner_id": learner["learner_id"], "item_id": iid, "correct": correct})

    return items, learners, responses
