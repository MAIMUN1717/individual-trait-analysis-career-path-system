class RoleMatcher:

    @staticmethod
    def check_eligibility(traits, eligibility_rules):
        if not eligibility_rules:
            return True

        for trait, min_value in eligibility_rules.items():
            if traits.get(trait, 0.0) < min_value:
                return False

        return True

    @staticmethod
    def compute_fit(traits, role_req):
        score = 0.0
        matched = []
        weak = []

        for trait, weight in role_req.trait_weights.items():
            value = traits.get(trait, 0.0)
            contribution = value * weight
            score += contribution

            if value >= 0.6:
                matched.append(trait)
            else:
                weak.append(trait)

        return round(score, 4), matched, weak
