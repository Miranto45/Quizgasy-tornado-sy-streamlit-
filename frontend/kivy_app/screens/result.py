from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class ResultScreen(Screen):
    summary = StringProperty("")
    details = StringProperty("")

    def show(self, res: dict, questions: list):
        by_id = {q["id"]: q for q in questions}
        lines = []
        for d in res["details"]:
            if not d["correct"]:
                q = by_id[d["id"]]
                lines.append(f"[b]{q['question']}[/b]\nValiny marina: {q['choices'][d['correct_index']]}\n"
                             f"{d['explanation']}\n")
        self.summary = f"{res['score']} / {res['total']}"
        self.details = "\n".join(lines) or "Tsara be! Marina daholo ny valinao!"
