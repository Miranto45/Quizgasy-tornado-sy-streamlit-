"""Fanadinana Madagasikara - backend FastAPI (port 8000)
Lancer : uvicorn main:app --reload --host 0.0.0.0 --port 8000   (docs : /docs)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # -> backend/ (pour `core`)

from fastapi import FastAPI  # noqa: E402
from fastapi.responses import JSONResponse  # noqa: E402

from core.errors import CoreError  # noqa: E402
from routers import auth, quiz, stats  # noqa: E402

app = FastAPI(title="Fanadinana Madagasikara (FastAPI)", version="2.0")


@app.exception_handler(CoreError)
async def core_error(request, exc: CoreError):
    return JSONResponse({"detail": exc.detail}, status_code=exc.status)


@app.get("/health", tags=["system"])
def health():
    return {"status": "ok", "server": "fastapi"}


app.include_router(auth.router)
app.include_router(quiz.router)
app.include_router(stats.router)
