from pydantic import BaseModel
from typing import List, Dict


class Answer(BaseModel):
    question_id: str
    selected_option: int


class AnalyzeRequest(BaseModel):
    answers: List[Answer]


class RoleExplanation(BaseModel):
    summary: str
    strengths: List[str]
    gaps: List[str]
    growth_suggestions: List[str]


class RoleResult(BaseModel):
    role: str
    fit_score: float
    explanation: RoleExplanation


class AnalyzeResponse(BaseModel):
    traits: Dict[str, float]
    recommendations: List[RoleResult]
