"""Fanadinana Madagasikara - backend Tornado (port 8001)
Même API REST que la version FastAPI + WebSocket /ws + page live sur /.
Lancer : python server.py     ->  http://localhost:8001
(sqlite et pbkdf2 sont synchrones : suffisant pour une démo)
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # -> backend/ (pour `core`)

import tornado.ioloop  # noqa: E402

import settings  # noqa: E402
from application import make_app  # noqa: E402
from realtime.hub import hub  # noqa: E402


async def main():
    hub.load()
    make_app().listen(settings.PORT, address="0.0.0.0")
    tornado.ioloop.PeriodicCallback(hub.refresh, settings.REFRESH_MS).start()
    print(f"Tornado : http://localhost:{settings.PORT}  (API REST + WebSocket /ws)")
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
