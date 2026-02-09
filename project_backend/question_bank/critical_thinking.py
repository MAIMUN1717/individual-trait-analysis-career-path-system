from core.questions_schema import Question, QuestionType, Priority

CRITICAL_THINKING_QUESTIONS = [

    # ─────────────────────────────
    # PROBLEM FRAMING (4)
    # ─────────────────────────────

    Question(
        id="CT_PF_01",
        text="When you encounter a complex problem, what do you do first?",
        options=[
            "Start solving immediately",
            "Look for a similar solved problem",
            "Understand the problem and constraints clearly",
            "Ask someone else for a solution"
        ],
        correct_option=None,
        trait="problem_framing",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="CT_PF_02",
        text="How often do you clarify assumptions before attempting a solution?",
        options=[
            "Never",
            "Rarely",
            "Often",
            "Always"
        ],
        correct_option=None,
        trait="problem_framing",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="CT_PF_03",
        text="If a problem statement is unclear, what do you usually do?",
        options=[
            "Proceed anyway",
            "Make assumptions silently",
            "Seek clarification",
            "Ignore the problem"
        ],
        correct_option=None,
        trait="problem_framing",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="CT_PF_04",
        text="Do you break large problems into smaller parts before solving?",
        options=[
            "Never",
            "Sometimes",
            "Most of the time",
            "Always"
        ],
        correct_option=None,
        trait="problem_framing",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # ANALYTICAL EVALUATION (4)
    # ─────────────────────────────

    Question(
        id="CT_AE_01",
        text="How do you decide whether a solution is effective?",
        options=[
            "By intuition",
            "By short-term results",
            "By checking against defined criteria",
            "By long-term impact"
        ],
        correct_option=None,
        trait="analytical_evaluation",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="CT_AE_02",
        text="When reviewing your own solution, what do you focus on most?",
        options=[
            "Speed of completion",
            "Ease of implementation",
            "Accuracy and logic",
            "Whether others agree"
        ],
        correct_option=None,
        trait="analytical_evaluation",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="CT_AE_03",
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
        priority=Priority.MEDIUM
    ),

    Question(
        id="CT_AE_04",
        text="Do you test multiple approaches before finalizing a solution?",
        options=[
            "Never",
            "Rarely",
            "Sometimes",
            "Often"
        ],
        correct_option=None,
        trait="analytical_evaluation",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # EVIDENCE JUDGMENT (4)
    # ─────────────────────────────

    Question(
        id="CT_EJ_01",
        text="When evaluating an argument, what influences you the most?",
        options=[
            "Who is presenting it",
            "Confidence of the speaker",
            "Supporting evidence",
            "Popularity of the opinion"
        ],
        correct_option=None,
        trait="evidence_judgment",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="CT_EJ_02",
        text="If evidence contradicts your belief, how do you respond?",
        options=[
            "Ignore the evidence",
            "Question the source",
            "Re-evaluate your belief",
            "Defend your belief strongly"
        ],
        correct_option=None,
        trait="evidence_judgment",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="CT_EJ_03",
        text="How often do you verify information before accepting it?",
        options=[
            "Never",
            "Rarely",
            "Often",
            "Always"
        ],
        correct_option=None,
        trait="evidence_judgment",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="CT_EJ_04",
        text="Do you rely more on data or opinions when making judgments?",
        options=[
            "Mostly opinions",
            "More opinions than data",
            "More data than opinions",
            "Mostly data"
        ],
        correct_option=None,
        trait="evidence_judgment",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # TRADE-OFF ANALYSIS (4)
    # ─────────────────────────────

    Question(
        id="CT_TO_01",
        text="When speed and accuracy conflict, what do you usually prioritize?",
        options=[
            "Speed",
            "Mostly speed",
            "Mostly accuracy",
            "Accuracy"
        ],
        correct_option=None,
        trait="tradeoff_analysis",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="CT_TO_02",
        text="How do you handle situations with no perfect solution?",
        options=[
            "Avoid deciding",
            "Delay the decision",
            "Choose the best compromise",
            "Let others decide"
        ],
        correct_option=None,
        trait="tradeoff_analysis",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="CT_TO_03",
        text="Do you consider long-term consequences when making decisions?",
        options=[
            "Never",
            "Rarely",
            "Often",
            "Always"
        ],
        correct_option=None,
        trait="tradeoff_analysis",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="CT_TO_04",
        text="When resources are limited, how do you proceed?",
        options=[
            "Use resources without planning",
            "Focus on immediate needs",
            "Balance needs carefully",
            "Optimize for maximum impact"
        ],
        correct_option=None,
        trait="tradeoff_analysis",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),
]
