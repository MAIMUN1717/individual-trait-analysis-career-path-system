from core.questions_schema import Question, QuestionType, Priority

DECISION_MAKING_QUESTIONS = [

    # ─────────────────────────────
    # RISK TOLERANCE (8)
    # ─────────────────────────────

    Question(
        id="DM_RT_01",
        text="When making an important decision, how comfortable are you taking calculated risks?",
        options=["Not comfortable", "Slightly comfortable", "Comfortable", "Very comfortable"],
        correct_option=None,
        trait="risk_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="DM_RT_02",
        text="If a solution has a high reward but also a high chance of failure, what do you do?",
        options=[
            "Avoid it completely",
            "Consider only if necessary",
            "Evaluate and possibly try",
            "Actively pursue it"
        ],
        correct_option=None,
        trait="risk_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="DM_RT_03",
        text="How do you usually feel about experimenting with untested approaches?",
        options=["Very uncomfortable", "Uncomfortable", "Comfortable", "Very comfortable"],
        correct_option=None,
        trait="risk_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="DM_RT_04",
        text="Do you prefer safe, proven methods over innovative ones?",
        options=["Strongly prefer safe methods", "Prefer safe methods", "Prefer innovative methods", "Strongly prefer innovation"],
        correct_option=None,
        trait="risk_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="DM_RT_05",
        text="How often do you take initiative when the outcome is uncertain?",
        options=["Never", "Rarely", "Often", "Very often"],
        correct_option=None,
        trait="risk_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="DM_RT_06",
        text="When faced with a risky choice, what guides you most?",
        options=["Fear of failure", "Past experiences", "Potential gain", "Opportunity to learn"],
        correct_option=None,
        trait="risk_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="DM_RT_07",
        text="Do you feel comfortable making decisions without complete information?",
        options=["Not at all", "Slightly", "Moderately", "Very comfortable"],
        correct_option=None,
        trait="risk_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    Question(
        id="DM_RT_08",
        text="How do you react when a risky decision fails?",
        options=["Avoid risks next time", "Feel discouraged", "Analyze and adjust", "Try again differently"],
        correct_option=None,
        trait="risk_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    # ─────────────────────────────
    # AMBIGUITY TOLERANCE (8)
    # ─────────────────────────────

    Question(
        id="DM_AT_01",
        text="How do you feel when requirements are unclear or changing?",
        options=["Very uncomfortable", "Uncomfortable", "Comfortable", "Very comfortable"],
        correct_option=None,
        trait="ambiguity_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="DM_AT_02",
        text="If a task has no clear instructions, what do you usually do?",
        options=[
            "Wait for clarity",
            "Ask for guidance",
            "Make assumptions and proceed",
            "Define your own approach"
        ],
        correct_option=None,
        trait="ambiguity_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="DM_AT_03",
        text="How comfortable are you working on problems with no single correct answer?",
        options=["Not comfortable", "Slightly comfortable", "Comfortable", "Very comfortable"],
        correct_option=None,
        trait="ambiguity_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.HIGH
    ),

    Question(
        id="DM_AT_04",
        text="When priorities change suddenly, how do you respond?",
        options=[
            "Get frustrated",
            "Feel stressed but adapt",
            "Re-prioritize calmly",
            "See it as an opportunity"
        ],
        correct_option=None,
        trait="ambiguity_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="DM_AT_05",
        text="Do you prefer well-defined tasks over open-ended challenges?",
        options=["Strongly prefer defined tasks", "Prefer defined tasks", "Prefer open-ended tasks", "Strongly prefer open-ended"],
        correct_option=None,
        trait="ambiguity_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="DM_AT_06",
        text="How do you manage uncertainty during long-term projects?",
        options=[
            "Avoid such projects",
            "Stick rigidly to initial plans",
            "Adjust plans when needed",
            "Continuously adapt"
        ],
        correct_option=None,
        trait="ambiguity_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.MEDIUM
    ),

    Question(
        id="DM_AT_07",
        text="Do unclear outcomes reduce your motivation?",
        options=["Very much", "Somewhat", "Slightly", "Not at all"],
        correct_option=None,
        trait="ambiguity_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),

    Question(
        id="DM_AT_08",
        text="How often do you seek certainty before making progress?",
        options=["Always", "Often", "Sometimes", "Rarely"],
        correct_option=None,
        trait="ambiguity_tolerance",
        qtype=QuestionType.BEHAVIORAL,
        priority=Priority.LOW
    ),
]
