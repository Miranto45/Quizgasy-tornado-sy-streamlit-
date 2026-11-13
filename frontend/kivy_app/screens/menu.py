from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class MenuScreen(Screen):
    stats = StringProperty("")

    def refresh(self):
        def ok(r):
            self.stats = f"Lalao: {r['games']}   |   Isa tsara indrindra: {r['best']}   |   Isa rehetra: {r['points']}"
        App.get_running_app().api.request("/me", ok)

    def logout(self):
        app = App.get_running_app()
        app.api.token, app.username = "", ""
        app.root.current = "login"
