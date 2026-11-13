from fastapi import APIRouter

from core.services import auth_service
from schemas import Credentials

router = APIRouter(tags=["auth"])


@router.post("/register")
def register(c: Credentials):
    return auth_service.register(c.username, c.password)


@router.post("/login")
def login(c: Credentials):
    return auth_service.login(c.username, c.password)
