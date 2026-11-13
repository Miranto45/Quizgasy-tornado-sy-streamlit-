
from pathlib import Path

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager

from api.client import ApiClient
from config import API, WS
from screens import BoardScreen, LoginScreen, MenuScreen, QuizScreen, ResultScreen
from services.live import LiveBoard

KV_DIR = Path(__file__).resolve().parent / "kv"
KV_FILES = ("base", "login", "menu", "quiz", "result", "board")  # base.kv d'abord (boutons)
Window.clearcolor = (0.07, 0.1, 0.09, 1)


class FanadinanaApp(App):
    username = StringProperty("")

    def build(self):
        self.title = "Fanadinana Madagasikara"
        self.api = ApiClient(API, on_error=self.popup)
        self.live = LiveBoard(WS)
        for name in KV_FILES:
            Builder.load_file(str(KV_DIR / f"{name}.kv"))
        sm = ScreenManager()
        for name, screen in (("login", LoginScreen), ("menu", MenuScreen), ("quiz", QuizScreen),
                             ("result", ResultScreen), ("board", BoardScreen)):
            sm.add_widget(screen(name=name))
        return sm

    def popup(self, message: str):
        Popup(title="Fampandrenesana", size_hint=(.85, .3),
              content=Label(text=message, text_size=(Window.width * .75, None), halign="center")).open()

    def on_stop(self):
        self.live.stop()


if __name__ == "__main__":
    FanadinanaApp().run()
