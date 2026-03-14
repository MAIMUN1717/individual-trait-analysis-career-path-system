from project_backend.engine.ranker import rank_roles
from project_backend.engine.explainer import RoleExplainer
from project_backend.engine.domain_predictor import predict_domain
from project_backend.roles.role_definitions import ROLES


def recommend_with_explanations(trait_vector: dict, standard_error: dict):

    detected_domain = predict_domain(trait_vector)

    ranked_roles = rank_roles(
        trait_vector,
        standard_error,
        domain=detected_domain
    )

    for role in ranked_roles:
        role_name = role["role"]
        role_traits = ROLES[role_name].trait_weights
        role["explanation"] = RoleExplainer.explain_with_gemini(role, trait_vector, role_traits, role_name)

    return {
        "domain": detected_domain,
        "recommendations": ranked_roles
    }