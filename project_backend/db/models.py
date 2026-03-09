from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from project_backend.db.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(150), unique=True, index=True)
    hashed_password = Column(String(255))
    created_at = Column(DateTime)

    sessions = relationship("TestSession", back_populates="user")


class TestSession(Base):
    __tablename__ = "test_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime)

    user = relationship("User", back_populates="sessions")
    results = relationship("RoleResult", back_populates="session")


class RoleResult(Base):
    __tablename__ = "role_results"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("test_sessions.id"))
    role_name = Column(String(100))
    fit_score = Column(Float)

    session = relationship("TestSession", back_populates="results")

class TraitEstimate(Base):
    __tablename__ = "trait_estimates"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("test_sessions.id"))
    trait_name = Column(String(100))
    theta_value = Column(Float)
    standard_error = Column(Float, nullable=True)