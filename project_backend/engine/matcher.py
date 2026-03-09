import math


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
    def compute_fit(traits, role_req, standard_error=None):

        role_traits = role_req.trait_weights

        score = cosine_similarity(traits, role_traits)

        # apply confidence weighting
        if standard_error:
            confidences = []

            for trait in role_traits:

                if trait in standard_error and standard_error[trait] is not None:
                    conf = 1 / (1 + standard_error[trait])
                    confidences.append(conf)

            if confidences:
                avg_conf = sum(confidences) / len(confidences)
                score = score * avg_conf

        matched = []
        weak = []

        for trait in role_traits:

            value = traits.get(trait, 0.0)

            if value >= 0.6:
                matched.append(trait)
            else:
                weak.append(trait)

        return round(score, 4), matched, weak


def cosine_similarity(user_traits, role_traits):

    dot = 0.0
    user_mag = 0.0
    role_mag = 0.0

    for trait, val in role_traits.items():

        u = user_traits.get(trait, 0.0)

        dot += u * val
        user_mag += u * u
        role_mag += val * val

    user_mag = math.sqrt(user_mag)
    role_mag = math.sqrt(role_mag)

    if user_mag == 0 or role_mag == 0:
        return 0.0

    return dot / (user_mag * role_mag)