import tornado.web

import settings
from realtime.hub import hub


class Index(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.write((settings.STATIC_DIR / "live.html").read_text(encoding="utf-8"))


class Health(tornado.web.RequestHandler):
    def get(self):
        self.write({"status": "ok", "server": "tornado", "online": len(hub.clients)})
