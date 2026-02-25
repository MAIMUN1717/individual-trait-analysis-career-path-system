from fastapi import APIRouter, Depends
from datetime import datetime
from sqlalchemy.orm import Session
import random
import time

from project_backend.engine.sampler import QuestionSampler
from project_backend.api.schemas import AnalyzeRequest, AnalyzeResponse
from project_backend.engine.scoring_pipeline import score_answers
from project_backend.engine.recommender import recommend_with_explanations

# ✅ Correct DB + Auth imports
from project_backend.db.db import get_db
from project_backend.db.models import User, TestSession, RoleResult
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
    trait_vector = score_answers(
        QUESTIONS,
        [ans.dict() for ans in request.answers]
    )

    recommendations = recommend_with_explanations(trait_vector)

    # SAVE SESSION
    session = TestSession(
        user_id=current_user.id,
        created_at=datetime.utcnow()
    )
    db.add(session)
    db.commit()
    db.refresh(session)

    # SAVE ROLE RESULTS
    for rec in recommendations:
        result = RoleResult(
            session_id=session.id,
            role_name=rec["role"],
            fit_score=rec["fit_score"]
        )
        db.add(result)

    db.commit()

    return {
        "traits": trait_vector,
        "recommendations": recommendations
    }


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