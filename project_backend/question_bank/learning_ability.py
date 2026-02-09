from core.questions_schema import Question, QuestionType, Priority

LEARNING_ABILITY_QUESTIONS = [

    # ─────────────────────────────
    # ADAPTABILITY (8)
    # ─────────────────────────────

    Question(
        id="LA_AD_01",
        text="When a new technology replaces an old one, how do you usually respond?",
        options=[
            "Avoid learning it",
            "Wait until required",
            "Learn it when needed",
            "Proactively explore it"
        ],
        correct_option=None,
        trait="adaptability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="LA_AD_02",
        text="How comfortable are you adapting your approach when requirements change?",
        options=["Very uncomfortable", "Uncomfortable", "Comfortable", "Very comfortable"],
        correct_option=None,
        trait="adaptability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="LA_AD_03",
        text="If a tool you mastered becomes obsolete, what do you do?",
        options=[
            "Stick with the old tool",
            "Avoid switching",
            "Switch reluctantly",
            "Switch and upskill"
        ],
        correct_option=None,
        trait="adaptability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="LA_AD_04",
        text="How often do you update your skills outside formal requirements?",
        options=["Never", "Rarely", "Often", "Very often"],
        correct_option=None,
        trait="adaptability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="LA_AD_05",
        text="How do you react when learning something feels difficult at first?",
        options=[
            "Give up quickly",
            "Feel discouraged",
            "Persist with effort",
            "Seek new strategies"
        ],
        correct_option=None,
        trait="adaptability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="LA_AD_06",
        text="Do you enjoy learning tools that are outside your comfort zone?",
        options=["Not at all", "A little", "Quite a bit", "Very much"],
        correct_option=None,
        trait="adaptability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="LA_AD_07",
        text="How quickly do you adjust when feedback suggests a different approach?",
        options=["Very slowly", "Slowly", "Quickly", "Very quickly"],
        correct_option=None,
        trait="adaptability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    Question(
        id="LA_AD_08",
        text="Do sudden changes in learning goals frustrate you?",
        options=["Very much", "Somewhat", "Slightly", "Not at all"],
        correct_option=None,
        trait="adaptability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # GROWTH MINDSET (8)
    # ─────────────────────────────

    Question(
        id="LA_GM_01",
        text="I believe my abilities can improve with consistent effort.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="growth_mindset",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="LA_GM_02",
        text="When I fail at something, I see it as a learning opportunity.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="growth_mindset",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="LA_GM_03",
        text="I enjoy challenging tasks that stretch my abilities.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="growth_mindset",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="LA_GM_04",
        text="If I struggle with a concept, I assume I’m just not good at it.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="growth_mindset",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="LA_GM_05",
        text="Feedback helps me improve my performance.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="growth_mindset",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="LA_GM_06",
        text="I believe effort is more important than talent for success.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="growth_mindset",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="LA_GM_07",
        text="I get discouraged easily when learning becomes challenging.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="growth_mindset",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    Question(
        id="LA_GM_08",
        text="I actively seek opportunities to learn new skills.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="growth_mindset",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),
]
