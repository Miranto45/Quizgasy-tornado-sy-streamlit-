"""Statistiques : classement général et profil."""
from contextlib import closing

from ..config import LEADERBOARD_SIZE
from ..database import connect


def leaderboard(limit: int = LEADERBOARD_SIZE) -> list:
    with closing(connect()) as con:
        rows = con.execute("""
            SELECT u.username, SUM(s.score) AS points, MAX(s.score) AS best, COUNT(*) AS games
            FROM scores s JOIN users u ON u.id = s.user_id
            GROUP BY u.id ORDER BY points DESC LIMIT ?""", (limit,)).fetchall()
    return [dict(r) for r in rows]


def me(user: dict) -> dict:
    with closing(connect()) as con:
        r = con.execute("SELECT COUNT(*) g, COALESCE(SUM(score),0) p, COALESCE(MAX(score),0) b "
                        "FROM scores WHERE user_id = ?", (user["id"],)).fetchone()
    return {"username": user["username"], "games": r["g"], "points": r["p"], "best": r["b"]}
