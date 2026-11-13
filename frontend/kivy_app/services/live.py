
import json
import threading

import websocket  # paquet websocket-client
from kivy.clock import Clock


class LiveBoard:
    def __init__(self, url: str):
        self.url, self.ws = url, None

    def start(self, on_open, on_rows, on_fail):
        self.stop()

        def _open(ws):
            Clock.schedule_once(lambda dt: on_open())

        def _message(ws, msg):
            data = json.loads(msg)
            Clock.schedule_once(lambda dt: on_rows(data["rows"], data.get("online")))

        def _error(ws, err):
            Clock.schedule_once(lambda dt: on_fail())

        self.ws = websocket.WebSocketApp(self.url, on_open=_open, on_message=_message, on_error=_error)
        threading.Thread(target=self.ws.run_forever, daemon=True).start()

    def stop(self):
        if self.ws:
            try:
                self.ws.close()
            except Exception:
                pass
            self.ws = None
