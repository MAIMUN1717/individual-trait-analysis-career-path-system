from roles.role_definitions import ROLES
from engine.matcher import RoleMatcher


def rank_roles(trait_vector: dict):
    results = []

    for role_name, role_req in ROLES.items():

        eligible = RoleMatcher.check_eligibility(
            trait_vector,
            role_req.eligibility
        )

        if not eligible:
            continue

        fit_score, matched, weak = RoleMatcher.compute_fit(
            trait_vector,
            role_req
        )

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
