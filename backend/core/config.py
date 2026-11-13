"""Réglages communs aux backends."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = os.environ.get("FANADINANA_DB", str(ROOT / "data" / "quiz.db"))

PBKDF2_ITERATIONS = 100_000
USERNAME_LEN = (3, 20)
PASSWORD_LEN = (4, 64)
DEFAULT_QUIZ_SIZE = 10
LEADERBOARD_SIZE = 10
