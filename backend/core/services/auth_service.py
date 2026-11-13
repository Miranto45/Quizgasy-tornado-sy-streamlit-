"""Comptes : inscription, connexion, jetons."""
import hashlib
import os
import secrets
import sqlite3
from contextlib import closing

from ..config import PASSWORD_LEN, PBKDF2_ITERATIONS, USERNAME_LEN
from ..database import connect
from ..errors import CoreError


def _hash(password: str, salt: str) -> str:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), PBKDF2_ITERATIONS).hex()


def _new_token(con, user_id: int) -> str:
    token = secrets.token_hex(24)
    con.execute("INSERT INTO tokens(token, user_id) VALUES(?, ?)", (token, user_id))
    con.commit()
    return token


def _check(username, password) -> None:
    lo, hi = USERNAME_LEN
    if not isinstance(username, str) or not lo <= len(username) <= hi:
        raise CoreError(422, f"Anarana: litera {lo} hatramin'ny {hi}")
    lo, hi = PASSWORD_LEN
    if not isinstance(password, str) or not lo <= len(password) <= hi:
        raise CoreError(422, f"Teny miafina: litera {lo} hatramin'ny {hi}")


def register(username, password) -> dict:
    _check(username, password)
    salt = os.urandom(16).hex()
    with closing(connect()) as con:
        try:
            cur = con.execute("INSERT INTO users(username, salt, pw_hash) VALUES(?,?,?)",
                              (username, salt, _hash(password, salt)))
        except sqlite3.IntegrityError:
            raise CoreError(400, "Efa misy ny anarana ampiasainao")
        con.commit()
        return {"token": _new_token(con, cur.lastrowid), "username": username}


def login(username, password) -> dict:
    _check(username, password)
    with closing(connect()) as con:
        user = con.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if not user or not secrets.compare_digest(user["pw_hash"], _hash(password, user["salt"])):
            raise CoreError(401, "Anarana na teny miafina diso")
        return {"token": _new_token(con, user["id"]), "username": user["username"]}


def user_for_token(token: str):
    """Renvoie {'id', 'username'} ou None si le jeton est inconnu."""
    with closing(connect()) as con:
        row = con.execute("SELECT u.id, u.username FROM tokens t JOIN users u ON u.id = t.user_id "
                          "WHERE t.token = ?", (token,)).fetchone()
    return dict(row) if row else None
