from project_backend.engine.irt_model import (
    update_theta as irt_update,
    item_information
)
from project_backend.engine.behavioral_engine import BehavioralEngine
from project_backend.engine.trait_covariance import apply_covariance

import math


class ThetaEngine:

    @staticmethod
    def estimate_theta(questions_by_id: dict, answers: list):

        theta = {}
        information = {}

        for ans in answers:
            q = questions_by_id.get(ans["question_id"])
            if not q:
                continue

            trait = q.trait

            if trait not in theta:
                theta[trait] = 0.0
                information[trait] = 0.0

            # ABILITY QUESTIONS
            if q.correct_option is not None:

                correct = ans["selected_option"] == q.correct_option

                theta[trait] = irt_update(
                    theta[trait],
                    q.discrimination_a,
                    q.difficulty_b,
                    correct
                )

                info = item_information(
                    theta[trait],
                    q.discrimination_a,
                    q.difficulty_b
                )

                information[trait] += info

            # BEHAVIORAL QUESTIONS
            else:

                theta[trait] = BehavioralEngine.update_theta(
                    theta[trait],
                    ans["selected_option"]
                )

        # Apply covariance adjustment between related traits
        theta = apply_covariance(theta)

        # Compute Standard Error
        standard_error = {}

        for trait, info in information.items():
            if info > 0:
                standard_error[trait] = 1 / math.sqrt(info)
            else:
                standard_error[trait] = None

        return theta, standard_error