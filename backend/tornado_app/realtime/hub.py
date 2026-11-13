"""Hub temps réel : liste des clients WebSocket + diffusion du classement."""
import asyncio
import json

import tornado.websocket

from core.services import stats_service


class LiveHub:
    def __init__(self):
        self.clients = set()
        self.last = []

    def load(self):
        self.last = stats_service.leaderboard()

    def add(self, client):
        self.clients.add(client)
        self.broadcast()

    def remove(self, client):
        self.clients.discard(client)
        self.broadcast()

    def broadcast(self):
        msg = json.dumps({"rows": self.last, "online": len(self.clients)})
        for c in list(self.clients):
            try:
                c.write_message(msg)
            except tornado.websocket.WebSocketClosedError:
                self.clients.discard(c)

    async def refresh(self):
        """Relit le classement et pousse aux clients s'il a changé."""
        board = await asyncio.get_running_loop().run_in_executor(None, stats_service.leaderboard)
        if board != self.last:
            self.last = board
            self.broadcast()


hub = LiveHub()
