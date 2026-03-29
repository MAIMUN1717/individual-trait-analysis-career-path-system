from .domain_models import DOMAIN_ARCHETYPES


def calculate_fit_score(domain, trait_scores):

    weights = DOMAIN_ARCHETYPES.get(domain)

    if not weights:
        return 0

    score = 0

    for trait, weight in weights.items():
        score += trait_scores.get(trait, 0) * weight

    return round(score, 2)