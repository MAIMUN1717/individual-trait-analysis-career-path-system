from dataclasses import dataclass
from enum import Enum
from typing import List
from core.traits import TRAITS


class QuestionType(Enum):
    ABILITY = "ability"
    BEHAVIORAL = "behavioral"


class QuestionPriority(Enum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1


@dataclass(frozen=True)
class Question:
    id: str
    text: str
    options: List[str]
    correct_option: int | None  # Only for ability questions
    trait: str                  # must exist in TRAITS
    qtype: QuestionType
    priority: QuestionPriority

QUESTIONS = [

    # 🧠 Cognitive Ability
    Question(
        id="LR_01",
        text="If all engineers are problem solvers and some problem solvers are designers, which statement is correct?",
        options=[
            "All designers are engineers",
            "Some designers may be engineers",
            "No engineers are designers",
            "All problem solvers are engineers"
        ],
        correct_option=1,
        trait="logical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=QuestionPriority.HIGH
    ),

    Question(
        id="AR_01",
        text="What comes next in the series: 2, 6, 12, 20, ?",
        options=["28", "30", "32", "36"],
        correct_option=1,
        trait="analytical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=QuestionPriority.HIGH
    ),

    # 🧩 Critical Thinking
    Question(
        id="CT_01",
        text="A project is delayed because a key assumption was wrong. What should you do first?",
        options=[
            "Blame the team",
            "Re-evaluate assumptions and revise the plan",
            "Continue with the same plan",
            "Wait for instructions"
        ],
        correct_option=None,
        trait="problem_framing",
        qtype=QuestionType.BEHAVIORAL,
        priority=QuestionPriority.HIGH
    ),

    # 🧬 Personality
    Question(
        id="P_01",
        text="How organized are you in managing tasks and deadlines?",
        options=[
            "Very disorganized",
            "Somewhat disorganized",
            "Fairly organized",
            "Highly organized"
        ],
        correct_option=None,
        trait="conscientiousness",
        qtype=QuestionType.BEHAVIORAL,
        priority=QuestionPriority.HIGH
    ),
]
