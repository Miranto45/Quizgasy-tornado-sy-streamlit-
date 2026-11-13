"""Dépendances FastAPI : authentification par jeton."""
from fastapi import Header, HTTPException

from core.services import auth_service


def current_user(authorization: str = Header(default="")) -> dict:
    user = auth_service.user_for_token(authorization.replace("Bearer ", "").strip())
    if not user:
        raise HTTPException(401, "Tsy mbola niditra ianao (token diso)")
    return user
