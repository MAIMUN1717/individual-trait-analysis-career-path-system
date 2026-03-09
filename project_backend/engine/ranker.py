from project_backend.roles.role_definitions import ROLES
from project_backend.engine.matcher import RoleMatcher


def rank_roles(trait_vector: dict, standard_error: dict, domain=None):

    results = []

    for role_name, role_req in ROLES.items():

        fit_score, matched, weak = RoleMatcher.compute_fit(
            trait_vector,
            role_req,
            standard_error
        )

        # Strong domain preference
        if domain and role_req.domain == domain:
            fit_score += 0.15

        results.append({
            "role": role_name,
            "fit_score": fit_score,
            "matched_traits": matched,
            "weak_traits": weak,
            "eligibility_passed": True
        })

    return sorted(
        results,
        key=lambda x: x["fit_score"],
        reverse=True
    )