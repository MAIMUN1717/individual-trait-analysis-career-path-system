from core.questions_schema import QuestionType
from core.scoring_base import (
    correctness_score,
    likert_to_score
)


class AnswerScorer:
    """
    Scores a single answer for a single question.
    """

    @staticmethod
    def score(question, selected_option: int) -> float:
        if question.qtype == QuestionType.ABILITY:
            return correctness_score(
                selected_option == question.correct_option
            )

        if question.qtype == QuestionType.BEHAVIORAL:
            # Likert assumed 1–4
            return likert_to_score(selected_option, scale_size=4)

        if question.qtype == QuestionType.CONTEXTUAL:
            # Contextual values handled separately
            return float(selected_option)

        raise ValueError("Unsupported question type")
