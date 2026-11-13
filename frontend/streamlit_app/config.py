
import os

DEFAULT_API = os.environ.get("FANADINANA_API", "http://127.0.0.1:8000")  # FastAPI :8000 | Tornado :8001
LIVE_URL = os.environ.get("FANADINANA_LIVE_URL", "http://localhost:8001")  # page live de Tornado
QUIZ_SIZE = 10
PAGES = ["Lalao", "Laharana", "Mombamomba"]
