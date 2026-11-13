
import streamlit as st

DEFAULTS = {"token": "", "username": "", "questions": [], "by_id": {}, "idx": 0, "answers": [], "result": None}


def init_state():
    for key, value in DEFAULTS.items():
        st.session_state.setdefault(key, value)


def reset_quiz():
    for key in ("questions", "by_id", "idx", "answers", "result"):
        st.session_state[key] = DEFAULTS[key].copy() if hasattr(DEFAULTS[key], "copy") else DEFAULTS[key]


def logout():
    st.session_state.token, st.session_state.username = "", ""
    reset_quiz()
