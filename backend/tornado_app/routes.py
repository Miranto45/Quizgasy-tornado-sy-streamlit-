"""Table des URL."""
from handlers.auth import Login, Register
from handlers.live import LiveWS
from handlers.pages import Health, Index
from handlers.quiz import Questions, Submit
from handlers.stats import Leaderboard, Me

ROUTES = [
    (r"/", Index),
    (r"/health", Health),
    (r"/ws", LiveWS),
    (r"/register", Register),
    (r"/login", Login),
    (r"/questions", Questions),
    (r"/submit", Submit),
    (r"/leaderboard", Leaderboard),
    (r"/me", Me),
]
