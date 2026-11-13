from fastapi import APIRouter, Depends

from core.config import DEFAULT_QUIZ_SIZE
from core.services import quiz_service
from dependencies import current_user
from schemas import Submission

router = APIRouter(tags=["quiz"])


@router.get("/questions")
def questions(n: int = DEFAULT_QUIZ_SIZE, user=Depends(current_user)):
    return quiz_service.public_questions(n)


@router.post("/submit")
def submit(s: Submission, user=Depends(current_user)):
    return quiz_service.submit(user["id"], [a.model_dump() for a in s.answers])
