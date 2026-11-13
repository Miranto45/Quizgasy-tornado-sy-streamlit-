"""Réglages du serveur Tornado."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
PORT = int(os.environ.get("PORT", 8001))
REFRESH_MS = 2000  # relecture du classement (scores venant aussi de FastAPI)
