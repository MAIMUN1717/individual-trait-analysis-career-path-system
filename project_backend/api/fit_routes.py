from fastapi import APIRouter, HTTPException
from project_backend.fit_check.controller import (
    generate_domain_questions,
    evaluate_answers
)
from project_backend.fit_check.domain_models import DOMAIN_TRAITS

router = APIRouter(prefix="/fit-check")


# ✅ GET ALL DOMAINS
@router.get("/domains")
def get_domains():
    return {"domains": list(DOMAIN_TRAITS.keys())}


# ✅ START FIT CHECK
@router.post("/start")
def start_fit_check(request: dict):

    domain = request.get("domain")

    if not domain:
        raise HTTPException(status_code=400, detail="Domain is required")

    if domain not in DOMAIN_TRAITS:
        raise HTTPException(status_code=400, detail="Invalid domain")

    questions = generate_domain_questions(domain)

    return {"questions": questions}


# ✅ SUBMIT ANSWERS
@router.post("/submit")
def submit_fit_check(request: dict):

    domain = request.get("domain")
    answers = request.get("answers")

    if not domain or not answers:
        raise HTTPException(status_code=400, detail="Invalid request")

    result = evaluate_answers(domain, answers)

    return result