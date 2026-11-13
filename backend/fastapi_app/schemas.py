"""Modèles Pydantic (corps des requêtes)."""
from pydantic import BaseModel


class Credentials(BaseModel):
    username: str
    password: str


class Answer(BaseModel):
    id: int
    choice: int


class Submission(BaseModel):
    answers: list[Answer]
