import tornado.websocket

from realtime.hub import hub


class LiveWS(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True  # démo scolaire

    def open(self):
        hub.add(self)

    def on_close(self):
        hub.remove(self)
