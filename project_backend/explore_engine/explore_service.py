from project_backend.explore_engine.domain_repository import DOMAINS


def get_all_domains():
    return [
        {
            "id": key,
            "name": value["name"]
        }
        for key, value in DOMAINS.items()
    ]


def get_domain(domain_id):
    domain = DOMAINS.get(domain_id)

    if not domain:
        return None

    return {
        "id": domain_id,
        "name": domain["name"],
        "overview": domain["overview"],
        "why_this_domain": domain["why_this_domain"],
        "core_concepts": domain["core_concepts"],
        "tools": domain["tools"],
        "roadmap": domain["roadmap"],
        "projects": domain["projects"],
        "interview_prep": domain["interview_prep"],
        "resources": domain["resources"]
    }