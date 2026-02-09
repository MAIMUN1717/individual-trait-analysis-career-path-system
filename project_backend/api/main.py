from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="FYP Career Recommendation Backend",
    description="Psychometric-based career recommendation system",
    version="1.0.0"
)

app.include_router(router)
