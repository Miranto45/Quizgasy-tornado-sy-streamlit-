from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class BoardScreen(Screen):
    rows = StringProperty("")
    status = StringProperty("")

    def open(self):
        """Live via Tornado ; si indisponible, repli HTTP via le backend courant."""
        app = App.get_running_app()
        self.rows, self.status = "", "Mifandray amin'ny Tornado..."
        app.root.current = "board"
        app.live.start(
            on_open=lambda: setattr(self, "status", "Mivantana (live)"),
            on_rows=self._render,
            on_fail=self._http_fallback,
        )

    def leave(self):
        app = App.get_running_app()
        app.live.stop()
        app.root.current = "menu"

    def _http_fallback(self):
        App.get_running_app().api.request("/leaderboard", lambda rows: self._render(rows, None, live=False))

    def _render(self, rows, online, live=True):
        self.rows = "\n".join(f"{i}. {r['username']}  -  {r['points']} pts  (best {r['best']}, {r['games']} lalao)"
                              for i, r in enumerate(rows, 1)) or "Mbola tsy misy isa."
        self.status = (f"Mivantana (live) - {online} mpijery" if live
                       else "Tornado tsy mandeha - fandrefesana HTTP")
