from fastapi import APIRouter
from engine.sampler import QuestionSampler
from api.schemas import AnalyzeRequest, AnalyzeResponse
from engine.scoring_pipeline import score_answers
from engine.recommender import recommend_with_explanations
from question_bank.cognitive_ability import COGNITIVE_ABILITY_QUESTIONS
from question_bank.critical_thinking import CRITICAL_THINKING_QUESTIONS
from question_bank.personality_big5 import PERSONALITY_QUESTIONS
from question_bank.decision_making import DECISION_MAKING_QUESTIONS
from question_bank.learning_ability import LEARNING_ABILITY_QUESTIONS
from question_bank.metacognition import METACOGNITION_QUESTIONS
from question_bank.attention_cognitive_load import ATTENTION_COGNITIVE_LOAD_QUESTIONS
from question_bank.interests_riasec import INTEREST_QUESTIONS
from question_bank.problem_solving import PROBLEM_SOLVING_QUESTIONS
from question_bank.academics import ACADEMIC_QUESTIONS




# Import all questions
from question_bank.cognitive_ability import COGNITIVE_ABILITY_QUESTIONS

router = APIRouter()

# Build question lookup
QUESTIONS = {
    q.id: q
    for q in (
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
}




@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):

    # Phase 3: score traits
    trait_vector = score_answers(
        QUESTIONS,
        [ans.dict() for ans in request.answers]
    )

    # Phase 4 + 5: recommend & explain
    recommendations = recommend_with_explanations(trait_vector)

    return {
        "traits": trait_vector,
        "recommendations": recommendations
    }
    
@router.get("/questions")
def get_questions(per_trait: int = 3):
    """
    Returns a shuffled, trait-balanced set of questions.
    """
    sampler = QuestionSampler(list(QUESTIONS.values()))
    selected_questions = sampler.sample_per_trait(per_trait=per_trait)

    return [
        {
            "id": q.id,
            "text": q.text,
            "options": q.options,
            "trait": q.trait
        }
        for q in selected_questions
    ]
