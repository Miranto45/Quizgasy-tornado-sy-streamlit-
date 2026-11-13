"""Code partagé par les backends FastAPI et Tornado. Importer `core` crée la base si besoin."""
from .database import init_db

init_db()
