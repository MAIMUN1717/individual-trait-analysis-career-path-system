# core/questions_schema.py

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
