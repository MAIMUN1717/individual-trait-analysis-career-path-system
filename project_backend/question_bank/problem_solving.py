from core.questions_schema import Question, QuestionType, Priority

PROBLEM_SOLVING_QUESTIONS = [

    # ─────────────────────────────
    # PROBLEM FRAMING (6)
    # ─────────────────────────────

    Question(
        id="PS_PF_01",
        text="When faced with a new problem, what is your first step?",
        options=[
            "Start trying solutions immediately",
            "Look for a similar solved problem",
            "Understand the problem and constraints clearly",
            "Ask someone else to handle it"
        ],
        correct_option=None,
        trait="problem_framing",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="PS_PF_02",
        text="If a problem statement is vague, how do you usually respond?",
        options=[
            "Proceed anyway",
            "Make assumptions silently",
            "Seek clarification",
            "Ignore the task"
        ],
        correct_option=None,
        trait="problem_framing",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="PS_PF_03",
        text="Do you break complex problems into smaller components?",
        options=["Never", "Sometimes", "Often", "Always"],
        correct_option=None,
        trait="problem_framing",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="PS_PF_04",
        text="How often do you clarify goals before starting to solve a problem?",
        options=["Never", "Rarely", "Often", "Always"],
        correct_option=None,
        trait="problem_framing",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="PS_PF_05",
        text="When solving problems, how important is understanding the context?",
        options=["Not important", "Slightly important", "Important", "Very important"],
        correct_option=None,
        trait="problem_framing",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="PS_PF_06",
        text="I prefer to solve problems without fully understanding them first.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="problem_framing",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # ANALYTICAL EVALUATION (6)
    # ─────────────────────────────

    Question(
        id="PS_AE_01",
        text="After attempting a solution, how do you evaluate its effectiveness?",
        options=[
            "By intuition",
            "By immediate results",
            "By testing against criteria",
            "By long-term impact"
        ],
        correct_option=None,
        trait="analytical_evaluation",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="PS_AE_02",
        text="If a solution works but feels inefficient, what do you do?",
        options=[
            "Accept it",
            "Ignore inefficiency",
            "Try to optimize it",
            "Discard it completely"
        ],
        correct_option=None,
        trait="analytical_evaluation",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="PS_AE_03",
        text="Do you compare multiple solutions before choosing one?",
        options=["Never", "Rarely", "Often", "Always"],
        correct_option=None,
        trait="analytical_evaluation",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="PS_AE_04",
        text="How do you respond when a chosen solution fails?",
        options=[
            "Give up",
            "Repeat the same approach",
            "Analyze and refine",
            "Seek external help"
        ],
        correct_option=None,
        trait="analytical_evaluation",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="PS_AE_05",
        text="Do you test your solutions under different scenarios?",
        options=["Never", "Rarely", "Often", "Always"],
        correct_option=None,
        trait="analytical_evaluation",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    Question(
        id="PS_AE_06",
        text="I rarely review solutions once they appear to work.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="analytical_evaluation",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # TRADE-OFF ANALYSIS (6)
    # ─────────────────────────────

    Question(
        id="PS_TO_01",
        text="When two solutions have different strengths, how do you decide?",
        options=[
            "Choose the faster one",
            "Choose the simpler one",
            "Weigh pros and cons",
            "Let others decide"
        ],
        correct_option=None,
        trait="tradeoff_analysis",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="PS_TO_02",
        text="How do you balance speed and quality in problem solving?",
        options=[
            "Always prioritize speed",
            "Usually prioritize speed",
            "Balance both",
            "Always prioritize quality"
        ],
        correct_option=None,
        trait="tradeoff_analysis",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="PS_TO_03",
        text="When resources are limited, what do you usually do?",
        options=[
            "Give up",
            "Focus on one aspect",
            "Balance resources carefully",
            "Optimize for maximum impact"
        ],
        correct_option=None,
        trait="tradeoff_analysis",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="PS_TO_04",
        text="Do you consider long-term effects when solving immediate problems?",
        options=["Never", "Rarely", "Often", "Always"],
        correct_option=None,
        trait="tradeoff_analysis",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="PS_TO_05",
        text="I am comfortable making decisions even when trade-offs are unclear.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="tradeoff_analysis",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    Question(
        id="PS_TO_06",
        text="I avoid decisions that involve significant compromises.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="tradeoff_analysis",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),
]
