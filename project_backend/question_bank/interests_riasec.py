from core.questions_schema import Question, QuestionType, Priority

INTEREST_QUESTIONS = [

    # ─────────────────────────────
    # REALISTIC (R) – Hands-on, Practical
    # ─────────────────────────────

    Question(
        id="IN_R_01",
        text="I enjoy working with physical systems, tools, or hardware.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="realistic_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),
    Question(
        id="IN_R_02",
        text="I prefer practical implementation over theoretical discussion.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="realistic_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # INVESTIGATIVE (I) – Analytical, Curious
    # ─────────────────────────────

    Question(
        id="IN_I_01",
        text="I enjoy analyzing data to discover patterns or insights.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="investigative_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="IN_I_02",
        text="I like exploring why systems behave the way they do.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="investigative_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="IN_I_03",
        text="I enjoy working with abstract concepts and models.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="investigative_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    # ─────────────────────────────
    # ARTISTIC (A) – Creative Expression
    # ─────────────────────────────

    Question(
        id="IN_A_01",
        text="I enjoy designing or creating visually appealing solutions.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="artistic_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),
    Question(
        id="IN_A_02",
        text="I like expressing ideas creatively rather than following strict rules.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="artistic_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # SOCIAL (S) – Helping, Teaching
    # ─────────────────────────────

    Question(
        id="IN_S_01",
        text="I enjoy helping others solve their problems.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="social_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),
    Question(
        id="IN_S_02",
        text="I like explaining concepts to people who are new to them.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="social_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    # ─────────────────────────────
    # ENTERPRISING (E) – Leadership, Influence
    # ─────────────────────────────

    Question(
        id="IN_E_01",
        text="I enjoy taking initiative and leading projects.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="enterprising_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),
    Question(
        id="IN_E_02",
        text="I am motivated by opportunities to influence outcomes.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="enterprising_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # CONVENTIONAL (C) – Structure, Order
    # ─────────────────────────────

    Question(
        id="IN_C_01",
        text="I prefer structured tasks with clear rules and procedures.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="conventional_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),
    Question(
        id="IN_C_02",
        text="I enjoy organizing information and maintaining order.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="conventional_interest",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # TECH DOMAIN PREFERENCE
    # ─────────────────────────────

    Question(
        id="IN_T_01",
        text="I am strongly interested in working in technology-related fields.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="tech_domain_preference",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="IN_T_02",
        text="I actively follow trends in software, data, or emerging technologies.",
        options=["Never", "Rarely", "Often", "Very often"],
        correct_option=None,
        trait="tech_domain_preference",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
    Question(
        id="IN_T_03",
        text="I enjoy building or experimenting with technical tools and systems.",
        options=["Strongly disagree", "Disagree", "Agree", "Strongly agree"],
        correct_option=None,
        trait="tech_domain_preference",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),
]
