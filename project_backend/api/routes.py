from fastapi import APIRouter, Depends
from datetime import datetime
from sqlalchemy.orm import Session
import random
import time
from pydantic import BaseModel
from typing import List

from project_backend.engine.sampler import QuestionSampler
from project_backend.api.schemas import AnalyzeRequest, AnalyzeResponse
from project_backend.engine.scoring_pipeline import score_answers
from project_backend.engine.recommender import recommend_with_explanations
from project_backend.engine.question_selector import AdaptiveQuestionSelector


# ✅ Correct DB + Auth imports
from project_backend.db.db import get_db
from project_backend.db.models import User, TestSession, RoleResult, TraitEstimate
from project_backend.auth.dependencies import get_current_user

# Question banks
from project_backend.question_bank.cognitive_ability import COGNITIVE_ABILITY_QUESTIONS
from project_backend.question_bank.critical_thinking import CRITICAL_THINKING_QUESTIONS
from project_backend.question_bank.personality_big5 import PERSONALITY_QUESTIONS
from project_backend.question_bank.decision_making import DECISION_MAKING_QUESTIONS
from project_backend.question_bank.learning_ability import LEARNING_ABILITY_QUESTIONS
from project_backend.question_bank.metacognition import METACOGNITION_QUESTIONS
from project_backend.question_bank.attention_cognitive_load import ATTENTION_COGNITIVE_LOAD_QUESTIONS
from project_backend.question_bank.interests_riasec import INTEREST_QUESTIONS
from project_backend.question_bank.problem_solving import PROBLEM_SOLVING_QUESTIONS
from project_backend.question_bank.academics import ACADEMIC_QUESTIONS
router = APIRouter()

class NextQuestionRequest(BaseModel):
    theta: float
    answered_ids: List[str]

# 🔹 Build question lookup
ALL_QUESTIONS = (
    COGNITIVE_ABILITY_QUESTIONS
    + CRITICAL_THINKING_QUESTIONS
    + PERSONALITY_QUESTIONS
    + DECISION_MAKING_QUESTIONS
    + LEARNING_ABILITY_QUESTIONS
    + METACOGNITION_QUESTIONS
    + ATTENTION_COGNITIVE_LOAD_QUESTIONS
    + INTEREST_QUESTIONS
    + PROBLEM_SOLVING_QUESTIONS
    + ACADEMIC_QUESTIONS
)

QUESTIONS = {q.id: q for q in ALL_QUESTIONS}


# =====================================================
# ANALYZE ENDPOINT
# =====================================================

@router.post("/analyze")
def analyze(
    request: AnalyzeRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # ----------------------------
    # 1️⃣ Score (Dual Engine)
    # ----------------------------
    result = score_answers(
        QUESTIONS,
        [ans.dict() for ans in request.answers]
    )

    trait_vector = result["theta"]
    standard_error = result["standard_error"]

    print("Final Traits:", trait_vector)

    # ----------------------------
    # 2️⃣ Normalize Theta
    # ----------------------------
    normalized_traits = {}

    for trait, value in trait_vector.items():

        normalized = (value + 3) / 6

        # Clamp between 0 and 1
        normalized_traits[trait] = max(0.0, min(1.0, normalized))

    # ----------------------------
    # 3️⃣ Get Domain + Recommendations
    # ----------------------------
    recs = recommend_with_explanations(
        normalized_traits,
        standard_error
    )

    domain = recs["domain"]
    recommendations = recs["recommendations"]

    recommendations = sorted(
        recommendations,
        key=lambda x: x["fit_score"],
        reverse=True
    )

    top3 = recommendations[:3]

    # ----------------------------
    # 4️⃣ Save Test Session
    # ----------------------------
    session = TestSession(
        user_id=current_user.id,
        created_at=datetime.utcnow()
    )
    db.add(session)
    db.commit()
    db.refresh(session)

    # ----------------------------
    # 5️⃣ Save Role Results
    # ----------------------------
    for rec in top3:
        result_entry = RoleResult(
            session_id=session.id,
            role_name=rec["role"],
            fit_score=rec["fit_score"]
        )
        db.add(result_entry)

    db.commit()

    # ----------------------------
    # 6️⃣ Save Trait Estimates
    # ----------------------------
    for trait, value in trait_vector.items():
        theta_entry = TraitEstimate(
            session_id=session.id,
            trait_name=trait,
            theta_value=value,
            standard_error=standard_error.get(trait)
        )
        db.add(theta_entry)

    db.commit()

    # ----------------------------
    # 7️⃣ Return Response
    # ----------------------------
    return {
        "traits": normalized_traits,
        "standard_error": standard_error,
        "domain": domain,
        "recommendations": recommendations
    }


# =====================================================
# =====================================================
# QUESTIONS ENDPOINT (UPGRADED DISTRIBUTION MODEL)
# =====================================================


@router.get("/questions")
def get_questions():

    # Seed randomness per request (ensures new shuffle each time)
    random.seed(time.time())

    selected_questions = []

    trait_sources = [
        COGNITIVE_ABILITY_QUESTIONS,
        CRITICAL_THINKING_QUESTIONS,
        PERSONALITY_QUESTIONS,
        DECISION_MAKING_QUESTIONS,
        LEARNING_ABILITY_QUESTIONS,
        METACOGNITION_QUESTIONS,
        ATTENTION_COGNITIVE_LOAD_QUESTIONS,
        INTEREST_QUESTIONS,
        PROBLEM_SOLVING_QUESTIONS,
        ACADEMIC_QUESTIONS
    ]

    for trait_list in trait_sources:

        # Create a copy so original order is untouched
        shuffled = trait_list[:]

        # Smart shuffle
        random.shuffle(shuffled)

        # Always take first 3 after shuffle
        selected_questions.extend(shuffled[:3])

    # Final shuffle so traits aren't grouped visually
    random.shuffle(selected_questions)

    return [
        {
            "id": q.id,
            "text": q.text,
            "options": q.options,
            "trait": q.trait
        }
        for q in selected_questions
    ]


@router.post("/next-question")
def next_question(request: NextQuestionRequest):

    theta = request.theta
    answered_ids = request.answered_ids

    answered_set = set(answered_ids)

    remaining_questions = [
        q for q in QUESTIONS.values()
        if q.id not in answered_set
    ]   

    next_q = AdaptiveQuestionSelector.select_next_question(
        theta,
        remaining_questions
    )

    if not next_q:
        return {"status": "complete"}

    return {
        "question_id": next_q.id,
        "text": next_q.text,
        "options": next_q.options
    }


    