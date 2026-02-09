from core.questions_schema import Question, QuestionType, Priority

COGNITIVE_ABILITY_QUESTIONS = [

    # ─────────────────────────────
    # LOGICAL REASONING (6)
    # ─────────────────────────────

    Question(
        id="CA_LR_01",
        text="If all developers are programmers and some programmers are designers, which statement is definitely true?",
        options=[
            "All designers are developers",
            "Some designers may be developers",
            "No developers are designers",
            "All programmers are designers"
        ],
        correct_option=1,
        trait="logical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.HIGH
    ),

    Question(
        id="CA_LR_02",
        text="If statement A is true and statement B is false, which conclusion is valid?",
        options=[
            "A and B are both true",
            "A is true and B is false",
            "Both are false",
            "Cannot be determined"
        ],
        correct_option=1,
        trait="logical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.HIGH
    ),

    Question(
        id="CA_LR_03",
        text="All machines are tools. Some tools are computers. Which is correct?",
        options=[
            "All computers are machines",
            "Some computers may be machines",
            "No machines are computers",
            "All tools are computers"
        ],
        correct_option=1,
        trait="logical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.MEDIUM
    ),

    Question(
        id="CA_LR_04",
        text="If today is Monday, what day will it be after 10 days?",
        options=["Wednesday", "Thursday", "Friday", "Saturday"],
        correct_option=2,
        trait="logical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.MEDIUM
    ),

    Question(
        id="CA_LR_05",
        text="Which conclusion logically follows?",
        options=[
            "All cats are animals, so all animals are cats",
            "Some animals may be cats",
            "No animals are cats",
            "Cats cannot be animals"
        ],
        correct_option=1,
        trait="logical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.LOW
    ),

    Question(
        id="CA_LR_06",
        text="If no A is B and all B is C, which is true?",
        options=[
            "Some A is C",
            "No A is C",
            "All A is C",
            "Some C is A"
        ],
        correct_option=1,
        trait="logical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # ANALYTICAL REASONING (6)
    # ─────────────────────────────

    Question(
        id="CA_AR_01",
        text="What comes next in the sequence: 2, 6, 12, 20, ?",
        options=["28", "30", "32", "36"],
        correct_option=1,
        trait="analytical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.HIGH
    ),

    Question(
        id="CA_AR_02",
        text="Find the missing number: 5, 10, 20, 40, ?",
        options=["45", "60", "80", "100"],
        correct_option=2,
        trait="analytical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.HIGH
    ),

    Question(
        id="CA_AR_03",
        text="If a train travels 60 km in 1 hour, how far will it travel in 2.5 hours?",
        options=["120 km", "150 km", "180 km", "200 km"],
        correct_option=1,
        trait="analytical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.MEDIUM
    ),

    Question(
        id="CA_AR_04",
        text="A rectangle has a length twice its width. If width is 5, what is the area?",
        options=["25", "50", "75", "100"],
        correct_option=1,
        trait="analytical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.MEDIUM
    ),

    Question(
        id="CA_AR_05",
        text="If 3 machines produce 9 items in 3 minutes, how many items do 6 machines produce in 3 minutes?",
        options=["9", "12", "18", "27"],
        correct_option=2,
        trait="analytical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.LOW
    ),

    Question(
        id="CA_AR_06",
        text="Which number does not belong: 2, 4, 8, 16, 18?",
        options=["4", "8", "16", "18"],
        correct_option=3,
        trait="analytical_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # ABSTRACT REASONING (6)
    # ─────────────────────────────

    Question(
        id="CA_AB_01",
        text="Which figure completes the pattern logically?",
        options=["Option A", "Option B", "Option C", "Option D"],
        correct_option=2,
        trait="abstract_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.HIGH
    ),

    Question(
        id="CA_AB_02",
        text="If ▲ is to ■ as ● is to ?",
        options=["▲", "■", "◆", "●"],
        correct_option=2,
        trait="abstract_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.HIGH
    ),

    Question(
        id="CA_AB_03",
        text="Which pattern follows: AB, CD, EF, ?",
        options=["GH", "GI", "FG", "HI"],
        correct_option=0,
        trait="abstract_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.MEDIUM
    ),

    Question(
        id="CA_AB_04",
        text="Find the odd one out: Square, Circle, Triangle, Cube",
        options=["Square", "Circle", "Triangle", "Cube"],
        correct_option=3,
        trait="abstract_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.MEDIUM
    ),

    Question(
        id="CA_AB_05",
        text="Which symbol does not follow the pattern?",
        options=["@", "#", "$", "A"],
        correct_option=3,
        trait="abstract_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.LOW
    ),

    Question(
        id="CA_AB_06",
        text="Which figure best represents progression?",
        options=["Option A", "Option B", "Option C", "Option D"],
        correct_option=1,
        trait="abstract_reasoning",
        qtype=QuestionType.ABILITY,
        priority=Priority.LOW
    ),
]
