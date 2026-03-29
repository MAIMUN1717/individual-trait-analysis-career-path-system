ANSWER_MAP = {
    "strongly_agree": 5,
    "agree": 4,
    "neutral": 3,
    "disagree": 2,
    "strongly_disagree": 1
}


def normalize(score):
    return score / 5