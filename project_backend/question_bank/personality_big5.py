from core.questions_schema import Question, QuestionType, Priority

PERSONALITY_QUESTIONS = [

    # ─────────────────────────────
    # OPENNESS (4)
    # ─────────────────────────────

    Question(
        id="P_OP_01",
        text="I enjoy learning new concepts and exploring unfamiliar topics.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="openness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="P_OP_02",
        text="I am curious about how things work behind the scenes.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="openness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="P_OP_03",
        text="I enjoy experimenting with new tools or approaches at work.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="openness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),
    Question(
        id="P_OP_04",
        text="I prefer familiar routines over trying new methods.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="openness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # CONSCIENTIOUSNESS (4)
    # ─────────────────────────────

    Question(
        id="P_CO_01",
        text="I complete tasks thoroughly and meet deadlines reliably.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="conscientiousness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="P_CO_02",
        text="I plan my work carefully before starting.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="conscientiousness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="P_CO_03",
        text="I follow through on commitments even when tasks are difficult.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="conscientiousness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),
    Question(
        id="P_CO_04",
        text="I sometimes leave tasks unfinished.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="conscientiousness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # EXTRAVERSION (4)
    # ─────────────────────────────

    Question(
        id="P_EX_01",
        text="I feel comfortable communicating my ideas in a group.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="extraversion",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="P_EX_02",
        text="I enjoy collaborating and discussing ideas with others.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="extraversion",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="P_EX_03",
        text="I prefer working alone rather than interacting with many people.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="extraversion",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),
    Question(
        id="P_EX_04",
        text="I am energized by social interaction at work.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="extraversion",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # AGREEABLENESS (4)
    # ─────────────────────────────

    Question(
        id="P_AG_01",
        text="I cooperate well with others and value teamwork.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="agreeableness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="P_AG_02",
        text="I try to understand others’ perspectives during disagreements.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="agreeableness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="P_AG_03",
        text="I am willing to compromise to maintain harmony.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="agreeableness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),
    Question(
        id="P_AG_04",
        text="I find it difficult to work with people who disagree with me.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="agreeableness",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # EMOTIONAL STABILITY (4)
    # ─────────────────────────────

    Question(
        id="P_ES_01",
        text="I remain calm and focused under pressure.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="emotional_stability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="P_ES_02",
        text="I handle work-related stress effectively.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="emotional_stability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="P_ES_03",
        text="Unexpected problems make me anxious.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="emotional_stability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),
    Question(
        id="P_ES_04",
        text="I recover quickly after stressful situations.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="emotional_stability",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),
]
