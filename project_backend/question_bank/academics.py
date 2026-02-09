from core.questions_schema import Question, QuestionType, Priority

ACADEMIC_QUESTIONS = [

    # ─────────────────────────────
    # DEGREE (4)
    # ─────────────────────────────

    Question(
        id="AC_DEG_01",
        text="What is your highest level of education?",
        options=[
            "Diploma",
            "Undergraduate",
            "Postgraduate",
            "Doctorate"
        ],
        correct_option=None,
        trait="degree",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="AC_DEG_02",
        text="Is your degree related to computer science or technology?",
        options=[
            "Not related",
            "Somewhat related",
            "Mostly related",
            "Fully related"
        ],
        correct_option=None,
        trait="degree",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="AC_DEG_03",
        text="How relevant do you feel your academic coursework is to real-world problems?",
        options=[
            "Not relevant",
            "Slightly relevant",
            "Relevant",
            "Highly relevant"
        ],
        correct_option=None,
        trait="degree",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="AC_DEG_04",
        text="Did your degree require significant analytical or technical work?",
        options=[
            "Very little",
            "Some",
            "Quite a lot",
            "A great deal"
        ],
        correct_option=None,
        trait="degree",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    # ─────────────────────────────
    # GPA (4)
    # ─────────────────────────────

    Question(
        id="AC_GPA_01",
        text="What is your approximate GPA or academic score range?",
        options=[
            "Below average",
            "Average",
            "Above average",
            "Excellent"
        ],
        correct_option=None,
        trait="gpa",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="AC_GPA_02",
        text="How consistent were your academic results over time?",
        options=[
            "Very inconsistent",
            "Somewhat inconsistent",
            "Mostly consistent",
            "Highly consistent"
        ],
        correct_option=None,
        trait="gpa",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="AC_GPA_03",
        text="Did your academic performance improve over time?",
        options=[
            "No improvement",
            "Slight improvement",
            "Moderate improvement",
            "Significant improvement"
        ],
        correct_option=None,
        trait="gpa",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="AC_GPA_04",
        text="How challenging did you find your academic curriculum?",
        options=[
            "Not challenging",
            "Somewhat challenging",
            "Challenging",
            "Very challenging"
        ],
        correct_option=None,
        trait="gpa",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # PROJECTS (4)
    # ─────────────────────────────

    Question(
        id="AC_PROJ_01",
        text="How many technical or academic projects have you completed?",
        options=[
            "None",
            "1–2 projects",
            "3–5 projects",
            "More than 5 projects"
        ],
        correct_option=None,
        trait="projects",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="AC_PROJ_02",
        text="How complex were the projects you worked on?",
        options=[
            "Very simple",
            "Moderately complex",
            "Complex",
            "Highly complex"
        ],
        correct_option=None,
        trait="projects",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="AC_PROJ_03",
        text="Did your projects involve problem-solving or real-world scenarios?",
        options=[
            "Not at all",
            "Somewhat",
            "Mostly",
            "Extensively"
        ],
        correct_option=None,
        trait="projects",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="AC_PROJ_04",
        text="How independently did you work on your projects?",
        options=[
            "Mostly assisted",
            "Partially independent",
            "Mostly independent",
            "Fully independent"
        ],
        correct_option=None,
        trait="projects",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),
]
