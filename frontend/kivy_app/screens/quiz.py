from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from config import QUIZ_SIZE


class QuizScreen(Screen):
    progress = StringProperty("")
    question = StringProperty("")
    questions: list = []
    answers: list = []
    idx = 0

    def start(self):
        app = App.get_running_app()

        def ok(qs):
            self.questions, self.answers, self.idx = qs, [], 0
            app.root.current = "quiz"
            self.show_question()

        app.api.request(f"/questions?n={QUIZ_SIZE}", ok)

    def show_question(self):
        q = self.questions[self.idx]
        self.progress = f"Fanontaniana {self.idx + 1} / {len(self.questions)}"
        self.question = q["question"]
        for i in range(4):
            self.ids[f"c{i}"].text = q["choices"][i]

    def answer(self, choice: int):
        if self.idx >= len(self.questions):
            return
        app = App.get_running_app()
        self.answers.append({"id": self.questions[self.idx]["id"], "choice": choice})
        self.idx += 1
        if self.idx < len(self.questions):
            self.show_question()
            return

        def done(res):
            app.root.get_screen("result").show(res, self.questions)
            app.root.current = "result"
            app.root.get_screen("menu").refresh()

        def retry():  # échec réseau : on revient sur la dernière question
            self.idx -= 1
            self.answers.pop()

        app.api.request("/submit", done, {"answers": self.answers}, on_fail=retry)
