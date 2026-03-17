from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi import Depends
from project_backend.api.routes import router
from project_backend.auth.auth_routes import router as auth_router
from project_backend.auth.dependencies import get_current_user
from project_backend.db.models import User
from project_backend.db.models import User, TestSession, RoleResult
from project_backend.db.db import get_db
from .fit_routes import router as fit_router
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="FYP Career Recommendation Backend",
    description="Psychometric-based career recommendation system",
    version="1.0.0"
)

app.include_router(router)
app.include_router(auth_router)
app.include_router(fit_router)

@app.get("/profile")
def profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }

from project_backend.db.models import TestSession, RoleResult


@app.get("/my-results")
def get_my_results(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    sessions = (
        db.query(TestSession)
        .filter(TestSession.user_id == current_user.id)
        .order_by(TestSession.created_at.desc())
        .all()
    )

    response = []

    for session in sessions:
        # Get highest scoring role for that session
        top_result = (
            db.query(RoleResult)
            .filter(RoleResult.session_id == session.id)
            .order_by(RoleResult.fit_score.desc())
            .first()
        )

        if top_result:
            response.append({
                "session_id": session.id,
                "created_at": session.created_at.strftime("%Y-%m-%d") if session.created_at else "",
                "top_role": top_result.role_name,
                "top_score": top_result.fit_score
            })

    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
