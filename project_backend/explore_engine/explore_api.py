from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from project_backend.explore_engine.explore_service import get_all_domains, get_domain
from project_backend.explore_engine.concept_expander import expand_concept

router = APIRouter(prefix="/explore", tags=["Explore"])


# ------------------------
# Request Model
# ------------------------
class ExpandRequest(BaseModel):
    domain: str
    concept: str


# ------------------------
# Routes
# ------------------------

@router.get("/domains")
def domains():
    return get_all_domains()


@router.get("/{domain_id}")
def domain_details(domain_id: str):
    domain = get_domain(domain_id)

    if not domain:
        raise HTTPException(status_code=404, detail="Domain not found")

    return domain


@router.post("/expand")
def expand(req: ExpandRequest):
    try:
        result = expand_concept(req.domain, req.concept)

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }