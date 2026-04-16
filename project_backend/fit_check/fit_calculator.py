from .domain_models import DOMAIN_ARCHETYPES


def calculate_fit_score(domain, trait_scores):

    weights = DOMAIN_ARCHETYPES.get(domain, {}).get("traits", {})

    if not weights:
        return 0

    score = 0

    for trait, weight in weights.items():
        normalized_trait = trait.lower().replace(" ", "_")
        score += float(trait_scores.get(normalized_trait, 0)) * float(weight)

    return round(score, 2)