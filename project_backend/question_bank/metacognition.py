from core.questions_schema import Question, QuestionType, Priority

METACOGNITION_QUESTIONS = [

    # ─────────────────────────────
    # PLANNING & MONITORING (8)
    # ─────────────────────────────

    Question(
        id="MC_PM_01",
        text="Before starting an important task, how do you usually proceed?",
        options=[
            "Start immediately",
            "Think briefly about steps",
            "Plan steps and resources",
            "Create a detailed plan"
        ],
        correct_option=None,
        trait="planning_and_monitoring",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="MC_PM_02",
        text="Do you set clear goals before beginning a task?",
        options=["Never", "Rarely", "Often", "Always"],
        correct_option=None,
        trait="planning_and_monitoring",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="MC_PM_03",
        text="How often do you track your progress while working on a task?",
        options=["Never", "Rarely", "Often", "Always"],
        correct_option=None,
        trait="planning_and_monitoring",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="MC_PM_04",
        text="If you realize you are falling behind schedule, what do you do?",
        options=[
            "Ignore it",
            "Rush at the end",
            "Adjust the plan",
            "Re-plan completely"
        ],
        correct_option=None,
        trait="planning_and_monitoring",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="MC_PM_05",
        text="Do you estimate time and effort before starting tasks?",
        options=["Never", "Rarely", "Often", "Always"],
        correct_option=None,
        trait="planning_and_monitoring",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="MC_PM_06",
        text="How do you manage multiple tasks with competing deadlines?",
        options=[
            "Work randomly",
            "Focus on one and ignore others",
            "Prioritize tasks",
            "Create a structured schedule"
        ],
        correct_option=None,
        trait="planning_and_monitoring",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="MC_PM_07",
        text="Do you review your plan during task execution?",
        options=["Never", "Rarely", "Sometimes", "Often"],
        correct_option=None,
        trait="planning_and_monitoring",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    Question(
        id="MC_PM_08",
        text="How comfortable are you adjusting plans mid-task?",
        options=["Very uncomfortable", "Uncomfortable", "Comfortable", "Very comfortable"],
        correct_option=None,
        trait="planning_and_monitoring",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # SELF-REFLECTION (8)
    # ─────────────────────────────

    Question(
        id="MC_SR_01",
        text="After completing a task, do you reflect on what worked and what didn’t?",
        options=["Never", "Rarely", "Often", "Always"],
        correct_option=None,
        trait="self_reflection",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="MC_SR_02",
        text="How often do you analyze mistakes to avoid repeating them?",
        options=["Never", "Rarely", "Often", "Always"],
        correct_option=None,
        trait="self_reflection",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="MC_SR_03",
        text="If a strategy fails, what do you usually do?",
        options=[
            "Give up",
            "Repeat the same approach",
            "Try a different strategy",
            "Seek feedback and revise"
        ],
        correct_option=None,
        trait="self_reflection",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="MC_SR_04",
        text="Do you seek feedback to improve your performance?",
        options=["Never", "Rarely", "Often", "Always"],
        correct_option=None,
        trait="self_reflection",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="MC_SR_05",
        text="How do you react to constructive criticism?",
        options=[
            "Reject it",
            "Feel defensive",
            "Consider it carefully",
            "Actively apply it"
        ],
        correct_option=None,
        trait="self_reflection",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="MC_SR_06",
        text="Do you consciously adjust your approach based on past outcomes?",
        options=["Never", "Rarely", "Often", "Always"],
        correct_option=None,
        trait="self_reflection",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="MC_SR_07",
        text="I regularly think about how I can improve my working methods.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="self_reflection",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    Question(
        id="MC_SR_08",
        text="I prefer not to dwell on mistakes once a task is finished.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="self_reflection",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),
]
