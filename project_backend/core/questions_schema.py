from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class QuestionType(Enum):
    ABILITY = "ability"
    BEHAVIORAL = "behavioral"
    CONTEXTUAL = "contextual"


class Priority(Enum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1


@dataclass(frozen=True)
class Question:
    id: str
    text: str
    options: List[str]
    correct_option: Optional[int]
    trait: str
    qtype: QuestionType
    priority: Priority

    # IRT PARAMETERS
    difficulty_b: float = 0.0
    discrimination_a: float = 1.0
    guessing_c: float = 0.0