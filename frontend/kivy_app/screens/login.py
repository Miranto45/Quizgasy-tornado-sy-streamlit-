from kivy.app import App
from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    def submit(self, path: str, username: str, password: str):
        app = App.get_running_app()

        def ok(res):
            app.api.token, app.username = res["token"], res["username"]
            app.root.get_screen("menu").refresh()
            app.root.current = "menu"

        app.api.request(path, ok, {"username": username.strip(), "password": password})
