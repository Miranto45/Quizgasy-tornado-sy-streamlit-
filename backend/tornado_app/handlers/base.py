"""Classe de base des handlers REST."""
import json

import tornado.web

from core.services import auth_service


class ApiHandler(tornado.web.RequestHandler):
    def fail(self, status: int, detail: str):
        self.set_status(status)
        self.finish({"detail": detail})

    def write_list(self, items):
        """Tornado refuse write(list) : on sérialise nous-mêmes."""
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json.dumps(items))

    def json_body(self) -> dict:
        try:
            body = json.loads(self.request.body or b"{}")
        except ValueError:
            return {}
        return body if isinstance(body, dict) else {}

    def auth_user(self):
        """Renvoie l'utilisateur, ou répond 401 et renvoie None."""
        token = self.request.headers.get("Authorization", "").replace("Bearer ", "").strip()
        user = auth_service.user_for_token(token)
        if not user:
            self.fail(401, "Tsy mbola niditra ianao (token diso)")
        return user
