from engine.ranker import rank_roles
from engine.explainer import RoleExplainer


def recommend_with_explanations(trait_vector: dict):
    ranked_roles = rank_roles(trait_vector)

    for role in ranked_roles:
        role["explanation"] = RoleExplainer.explain(role)

    return ranked_roles
