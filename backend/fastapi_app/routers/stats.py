from fastapi import APIRouter, Depends

from core.services import stats_service
from dependencies import current_user

router = APIRouter(tags=["stats"])


@router.get("/leaderboard")
def leaderboard(user=Depends(current_user)):
    return stats_service.leaderboard()


@router.get("/me")
def me(user=Depends(current_user)):
    return stats_service.me(user)
