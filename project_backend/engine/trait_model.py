TRAIT_MODEL = {

    "analytical_reasoning": {
        "abstract_reasoning": 0.6,
        "tradeoff_analysis": 0.4
    },

    "problem_framing": {
        "tradeoff_analysis": 0.5,
        "planning_and_monitoring": 0.3,
        "projects": 0.2
    },

    "learning_agility": {
        "adaptability": 0.7,
        "ambiguity_tolerance": 0.3
    },

    "attention_control": {
        "planning_and_monitoring": 0.6,
        "self_reflection": 0.4
    },

    "creativity": {
        "projects": 0.6,
        "abstract_reasoning": 0.4
    },

    "decision_style": {
        "tradeoff_analysis": 0.7,
        "ambiguity_tolerance": 0.3
    }

}


def aggregate_traits(raw_traits: dict) -> dict:

    aggregated = {}

    for trait, components in TRAIT_MODEL.items():

        score = 0.0

        for comp, weight in components.items():

            score += float(raw_traits.get(comp, 0)) * weight

        aggregated[trait] = score

    return aggregated