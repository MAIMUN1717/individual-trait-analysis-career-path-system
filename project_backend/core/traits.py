from dataclasses import dataclass
from core.trait_types import TraitCategory, TraitType, ScoringMethod


@dataclass(frozen=True)
class Trait:
    name: str
    category: TraitCategory
    trait_type: TraitType
    scoring_method: ScoringMethod

TRAITS = {

    # 🧠 Cognitive Ability
    "logical_reasoning": Trait(
        "logical_reasoning",
        TraitCategory.COGNITIVE,
        TraitType.ABILITY,
        ScoringMethod.CORRECTNESS
    ),
    "analytical_reasoning": Trait(
        "analytical_reasoning",
        TraitCategory.COGNITIVE,
        TraitType.ABILITY,
        ScoringMethod.CORRECTNESS
    ),
    "abstract_reasoning": Trait(
        "abstract_reasoning",
        TraitCategory.COGNITIVE,
        TraitType.ABILITY,
        ScoringMethod.CORRECTNESS
    ),

    # 🧩 Critical Thinking
    "analytical_evaluation": Trait(
        "analytical_evaluation",
        TraitCategory.CRITICAL_THINKING,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "evidence_judgment": Trait(
        "evidence_judgment",
        TraitCategory.CRITICAL_THINKING,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "problem_framing": Trait(
        "problem_framing",
        TraitCategory.CRITICAL_THINKING,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "tradeoff_analysis": Trait(
        "tradeoff_analysis",
        TraitCategory.CRITICAL_THINKING,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),

    # 🧬 Personality (Big Five)
    "openness": Trait(
        "openness",
        TraitCategory.PERSONALITY,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "conscientiousness": Trait(
        "conscientiousness",
        TraitCategory.PERSONALITY,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "extraversion": Trait(
        "extraversion",
        TraitCategory.PERSONALITY,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "agreeableness": Trait(
        "agreeableness",
        TraitCategory.PERSONALITY,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "emotional_stability": Trait(
        "emotional_stability",
        TraitCategory.PERSONALITY,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),

    # 🎯 Interests (RIASEC + Tech)
    "realistic_interest": Trait(
        "realistic_interest",
        TraitCategory.INTERESTS,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "investigative_interest": Trait(
        "investigative_interest",
        TraitCategory.INTERESTS,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "artistic_interest": Trait(
        "artistic_interest",
        TraitCategory.INTERESTS,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "social_interest": Trait(
        "social_interest",
        TraitCategory.INTERESTS,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "enterprising_interest": Trait(
        "enterprising_interest",
        TraitCategory.INTERESTS,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "conventional_interest": Trait(
        "conventional_interest",
        TraitCategory.INTERESTS,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "tech_domain_preference": Trait(
        "tech_domain_preference",
        TraitCategory.INTERESTS,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),

    # ⚖️ Decision-Making
    "risk_tolerance": Trait(
        "risk_tolerance",
        TraitCategory.DECISION_MAKING,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "ambiguity_tolerance": Trait(
        "ambiguity_tolerance",
        TraitCategory.DECISION_MAKING,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),

    # 🚀 Learning Ability
    "adaptability": Trait(
        "adaptability",
        TraitCategory.LEARNING_ABILITY,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),
    "growth_mindset": Trait(
        "growth_mindset",
        TraitCategory.LEARNING_ABILITY,
        TraitType.BEHAVIORAL,
        ScoringMethod.LIKERT_SCALE
    ),

    # 📚 Academics
    "degree": Trait(
        "degree",
        TraitCategory.ACADEMICS,
        TraitType.CONTEXTUAL,
        ScoringMethod.DIRECT_VALUE
    ),
    "gpa": Trait(
        "gpa",
        TraitCategory.ACADEMICS,
        TraitType.CONTEXTUAL,
        ScoringMethod.DIRECT_VALUE
    ),
    "projects": Trait(
        "projects",
        TraitCategory.ACADEMICS,
        TraitType.CONTEXTUAL,
        ScoringMethod.DIRECT_VALUE
    ),
}
