from engine.templates import (
    TRAIT_DESCRIPTIONS,
    STRENGTH_TEMPLATE,
    WEAKNESS_TEMPLATE,
    OVERALL_TEMPLATE,
    GROWTH_TEMPLATE
)


class RoleExplainer:

    @staticmethod
    def explain(role_result: dict) -> dict:
        explanations = {
            "summary": OVERALL_TEMPLATE,
            "strengths": [],
            "gaps": [],
            "growth_suggestions": []
        }

        for trait in role_result.get("matched_traits", []):
            desc = TRAIT_DESCRIPTIONS.get(trait, trait)
            explanations["strengths"].append(
                STRENGTH_TEMPLATE.format(trait_desc=desc)
            )

        for trait in role_result.get("weak_traits", []):
            desc = TRAIT_DESCRIPTIONS.get(trait, trait)
            explanations["gaps"].append(
                WEAKNESS_TEMPLATE.format(trait_desc=desc)
            )
            explanations["growth_suggestions"].append(
                GROWTH_TEMPLATE.format(trait_desc=desc)
            )

        return explanations
