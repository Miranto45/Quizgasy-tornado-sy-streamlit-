"""Quiz : tirage des questions et correction côté serveur."""
import random
from contextlib import closing

from ..config import DEFAULT_QUIZ_SIZE
from ..data.questions import QUESTIONS
from ..database import connect
from ..errors import CoreError


def public_questions(n: int = DEFAULT_QUIZ_SIZE) -> list:
    """Questions aléatoires SANS la bonne réponse."""
    picked = random.sample(list(QUESTIONS.values()), min(max(n, 1), len(QUESTIONS)))
    return [{"id": q["id"], "question": q["question"], "choices": q["choices"]} for q in picked]


def submit(user_id: int, answers) -> dict:
    """Corrige les réponses, enregistre le score et renvoie le détail."""
    seen, details, score = set(), [], 0
    for a in answers if isinstance(answers, list) else []:
        try:
            qid, choice = int(a["id"]), int(a["choice"])
        except (KeyError, TypeError, ValueError):
            continue
        q = QUESTIONS.get(qid)
        if not q or qid in seen:
            continue
        seen.add(qid)
        ok = choice == q["answer"]
        score += ok
        details.append({"id": qid, "correct": ok, "correct_index": q["answer"],
                        "explanation": q["explanation"]})
    if not details:
        raise CoreError(400, "Tsy misy valiny")
    with closing(connect()) as con:
        con.execute("INSERT INTO scores(user_id, score, total) VALUES(?,?,?)",
                    (user_id, score, len(details)))
        con.commit()
    return {"score": score, "total": len(details), "details": details}
