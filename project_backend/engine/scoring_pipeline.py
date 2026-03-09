from project_backend.engine.theta_engine import ThetaEngine
from project_backend.engine.trait_model import aggregate_traits


def score_answers(questions_by_id: dict, answers: list):

    theta_vector, standard_error = ThetaEngine.estimate_theta(
        questions_by_id,
        answers
    )

    # Treat theta_vector as raw trait scores
    raw_traits = theta_vector

    # Aggregate traits into core psychometric traits
    final_traits = aggregate_traits(raw_traits)

    return {
        "theta": final_traits,
        "standard_error": standard_error
    }