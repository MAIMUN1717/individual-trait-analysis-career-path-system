from engine.scorer import AnswerScorer
from engine.aggregator import TraitAggregator


def score_answers(questions_by_id: dict, answers: list) -> dict:
    """
    Full scoring pipeline.
    """

    aggregator = TraitAggregator()

    for ans in answers:
        q = questions_by_id.get(ans["question_id"])
        if not q:
            continue

        score = AnswerScorer.score(q, ans["selected_option"])
        aggregator.add(q.trait, score)

    return aggregator.aggregate()
