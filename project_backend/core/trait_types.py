from enum import Enum


class TraitCategory(Enum):
    COGNITIVE = "cognitive_ability"
    CRITICAL_THINKING = "critical_thinking"
    PERSONALITY = "personality"
    INTERESTS = "interests"
    DECISION_MAKING = "decision_making"
    LEARNING_ABILITY = "learning_ability"
    ACADEMICS = "academics"


class TraitType(Enum):
    ABILITY = "ability"          # right / wrong
    BEHAVIORAL = "behavioral"    # likert / preference
    CONTEXTUAL = "contextual"    # degree, GPA, projects


class ScoringMethod(Enum):
    CORRECTNESS = "correctness"
    LIKERT_SCALE = "likert_scale"
    DIRECT_VALUE = "direct_value"
