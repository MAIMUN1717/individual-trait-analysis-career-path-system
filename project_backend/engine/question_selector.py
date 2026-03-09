import math


CONFIDENCE_THRESHOLD = 0.30


class AdaptiveQuestionSelector:

    @staticmethod
    def select_next_question(theta, questions, answered, standard_error=None):

        # Stop CAT if confidence is high enough
        if standard_error and min(
            [v for v in standard_error.values() if v is not None],
            default=1
        ) < CONFIDENCE_THRESHOLD:
            return None

        best_q = None
        best_info = -1

        for q in questions:

            if q.id in answered:
                continue

            # Skip if question lacks IRT parameters
            if q.discrimination_a is None or q.difficulty_b is None:
                continue

            info = item_information(theta, q)

            if info > best_info:
                best_info = info
                best_q = q

        return best_q


def item_information(theta, question):

    a = question.discrimination_a
    b = question.difficulty_b
    c = question.guessing_c if question.guessing_c is not None else 0

    try:

        p = c + (1 - c) / (1 + math.exp(-a * (theta - b)))

        info = (a * a * ((p - c) ** 2) * (1 - p)) / (((1 - c) ** 2) * p)

        return info

    except Exception:
        return 0