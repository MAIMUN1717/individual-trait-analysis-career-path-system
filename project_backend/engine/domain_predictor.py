import math
from project_backend.engine.domain_model import DOMAIN_ARCHETYPES


def cosine_similarity(user_traits, archetype):

    dot = 0
    user_mag = 0
    arch_mag = 0

    for t,v in archetype.items():

        u = user_traits.get(t,0)

        dot += u*v
        user_mag += u*u
        arch_mag += v*v

    user_mag = math.sqrt(user_mag)
    arch_mag = math.sqrt(arch_mag)

    if user_mag == 0 or arch_mag == 0:
        return 0

    return dot/(user_mag*arch_mag)


def predict_domain(traits):

    best_domain = None
    best_score = -1

    for domain, archetype in DOMAIN_ARCHETYPES.items():

        score = cosine_similarity(traits, archetype)

        if score > best_score:
            best_score = score
            best_domain = domain

    return best_domain