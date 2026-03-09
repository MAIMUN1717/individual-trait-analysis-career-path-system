class BehavioralEngine:

    LIKERT_MAPPING = {
        0: -1.5,
        1: -0.5,
        2: 0.5,
        3: 1.5
    }

    @staticmethod
    def update_theta(theta, selected_option, learning_rate=0.15):
        """
        Bayesian-style graded update for behavioral traits.
        """

        value = BehavioralEngine.LIKERT_MAPPING.get(selected_option, 0)

        # Move theta gradually toward expressed preference
        return theta + learning_rate * (value - theta)