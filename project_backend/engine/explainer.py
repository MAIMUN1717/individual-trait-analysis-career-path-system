from project_backend.engine.templates import (
    TRAIT_DESCRIPTIONS,
    STRENGTH_TEMPLATE,
    WEAKNESS_TEMPLATE,
    OVERALL_TEMPLATE,
    GROWTH_TEMPLATE
)


class RoleExplainer:

    @staticmethod
    def compute_trait_gaps(user_traits: dict, role_traits: dict) -> dict:
        """
        Calculate the gap between user traits and role requirements.
        Positive gap means the role expects higher ability.
        """

        gaps = {}

        for trait, required in role_traits.items():
            user_value = user_traits.get(trait, 0.0)
            gaps[trait] = round(required - user_value, 3)

        return gaps


    @staticmethod
    def explain(role_result: dict, user_traits: dict = None) -> dict:

        explanations = {
            "summary": OVERALL_TEMPLATE,
            "strengths": [],
            "gaps": [],
            "growth_suggestions": []
        }

        # strengths
        for trait in role_result.get("matched_traits", []):
            desc = TRAIT_DESCRIPTIONS.get(trait, trait)

            explanations["strengths"].append(
                STRENGTH_TEMPLATE.format(trait_desc=desc)
            )

        # weaknesses
        for trait in role_result.get("weak_traits", []):
            desc = TRAIT_DESCRIPTIONS.get(trait, trait)

            explanations["gaps"].append(
                WEAKNESS_TEMPLATE.format(trait_desc=desc)
            )

            explanations["growth_suggestions"].append(
                GROWTH_TEMPLATE.format(trait_desc=desc)
            )

        return explanations