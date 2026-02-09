from core.questions_schema import Question, QuestionType, Priority

ATTENTION_COGNITIVE_LOAD_QUESTIONS = [

    # ─────────────────────────────
    # FOCUS DURATION (8)
    # ─────────────────────────────

    Question(
        id="AT_FD_01",
        text="How long can you stay focused on a demanding task without getting distracted?",
        options=[
            "Less than 10 minutes",
            "10–20 minutes",
            "20–40 minutes",
            "More than 40 minutes"
        ],
        correct_option=None,
        trait="focus_duration",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="AT_FD_02",
        text="Do you find it easy to concentrate when working on complex problems?",
        options=["Not at all", "Slightly", "Moderately", "Very easily"],
        correct_option=None,
        trait="focus_duration",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="AT_FD_03",
        text="How often do external distractions affect your work?",
        options=["Very often", "Often", "Sometimes", "Rarely"],
        correct_option=None,
        trait="focus_duration",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="AT_FD_04",
        text="When interrupted, how quickly can you return to deep focus?",
        options=["Very slowly", "Slowly", "Quickly", "Very quickly"],
        correct_option=None,
        trait="focus_duration",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="AT_FD_05",
        text="Do you lose focus when tasks become repetitive?",
        options=["Very often", "Often", "Sometimes", "Rarely"],
        correct_option=None,
        trait="focus_duration",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="AT_FD_06",
        text="How well do you maintain concentration during long study or work sessions?",
        options=["Very poorly", "Poorly", "Well", "Very well"],
        correct_option=None,
        trait="focus_duration",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="AT_FD_07",
        text="I can stay focused even when tasks are mentally exhausting.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="focus_duration",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    Question(
        id="AT_FD_08",
        text="My attention drops significantly after working for a short time.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="focus_duration",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # COGNITIVE LOAD TOLERANCE (8)
    # ─────────────────────────────

    Question(
        id="AT_CL_01",
        text="How well do you handle multiple pieces of information at the same time?",
        options=["Very poorly", "Poorly", "Moderately well", "Very well"],
        correct_option=None,
        trait="cognitive_load_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="AT_CL_02",
        text="When working under pressure with many tasks, how do you perform?",
        options=[
            "Performance drops significantly",
            "Performance drops slightly",
            "Performance stays stable",
            "Performance improves"
        ],
        correct_option=None,
        trait="cognitive_load_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="AT_CL_03",
        text="Do you feel mentally overloaded when handling complex tasks?",
        options=["Very often", "Often", "Sometimes", "Rarely"],
        correct_option=None,
        trait="cognitive_load_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="AT_CL_04",
        text="How effectively can you prioritize when multiple demands compete?",
        options=["Very poorly", "Poorly", "Well", "Very well"],
        correct_option=None,
        trait="cognitive_load_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="AT_CL_05",
        text="When overwhelmed, what is your usual response?",
        options=[
            "Shut down",
            "Work randomly",
            "Slow down and organize",
            "Systematically manage load"
        ],
        correct_option=None,
        trait="cognitive_load_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="AT_CL_06",
        text="How comfortable are you juggling several responsibilities at once?",
        options=["Very uncomfortable", "Uncomfortable", "Comfortable", "Very comfortable"],
        correct_option=None,
        trait="cognitive_load_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="AT_CL_07",
        text="I can think clearly even when under heavy workload.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="cognitive_load_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    Question(
        id="AT_CL_08",
        text="High mental workload negatively affects my decision-making.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="cognitive_load_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),
]
