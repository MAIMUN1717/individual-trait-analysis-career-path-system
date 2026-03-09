COVARIANCE = {

    ("analytical_reasoning", "problem_framing"): 0.65,
    ("analytical_reasoning", "learning_agility"): 0.42,
    ("problem_framing", "creativity"): 0.38,
    ("attention_control", "learning_agility"): 0.40,
    ("decision_style", "problem_framing"): 0.33

}

ALPHA = 0.15


def apply_covariance(traits: dict) -> dict:
    """
    Adjust trait values using covariance relationships between traits.
    This stabilizes estimates when some traits have fewer questions.
    """

    adjusted = traits.copy()

    for (t1, t2), corr in COVARIANCE.items():

        if t1 in traits and t2 in traits:

            influence = float(corr) * float(traits[t2]) * ALPHA

            adjusted[t1] = adjusted.get(t1, 0.0) + influence

    return adjusted