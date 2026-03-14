from project_backend.engine.templates import (
    TRAIT_DESCRIPTIONS,
    STRENGTH_TEMPLATE,
    WEAKNESS_TEMPLATE,
    OVERALL_TEMPLATE,
    GROWTH_TEMPLATE
)
from project_backend.engine.gemini_service import GeminiService


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
    def explain_with_gemini(role_result: dict, user_traits: dict, role_traits: dict, role_name: str) -> dict:
        """
        Enhanced explanation using Gemini AI for personalized gap analysis
        while keeping existing template-based strengths
        """
        explanations = {
            "summary": OVERALL_TEMPLATE,
            "strengths": [],
            "gaps": [],
            "growth_suggestions": []
        }

        # Keep existing template-based strengths (no change)
        for trait in role_result.get("matched_traits", []):
            desc = TRAIT_DESCRIPTIONS.get(trait, trait)
            explanations["strengths"].append(
                STRENGTH_TEMPLATE.format(trait_desc=desc)
            )

        # Use Gemini for personalized gap analysis
        gemini_service = GeminiService()
        gaps = RoleExplainer.compute_trait_gaps(user_traits, role_traits)
        
        # Generate personalized gap analysis using Gemini
        personalized_gaps = gemini_service.analyze_trait_gaps(
            user_traits=user_traits,
            role_traits=role_traits,
            gaps=gaps,
            role_name=role_name
        )
        
        # Add Gemini response to both gaps and growth suggestions
        if personalized_gaps:
            explanations["gaps"].append(personalized_gaps)
            explanations["growth_suggestions"].append(personalized_gaps)

        return explanations


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