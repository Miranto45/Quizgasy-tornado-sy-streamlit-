
import streamlit as st

import config
import state
from api_client import call
from components.results import render_result


def render():
    S = st.session_state
    st.header("Lalao")
    if S.result:
        _result(S)
    elif not S.questions:
        _start(S)
    else:
        _question(S)


def _start(S):
    if st.button(f"Hanomboka ({config.QUIZ_SIZE} fanontaniana)", type="primary"):
        questions = call("GET", f"/questions?n={config.QUIZ_SIZE}")
        if questions:
            S.questions, S.idx, S.answers = questions, 0, []
            S.by_id = {q["id"]: q for q in questions}
            st.rerun()


def _question(S):
    q = S.questions[S.idx]
    st.progress(S.idx / len(S.questions), text=f"Fanontaniana {S.idx + 1} / {len(S.questions)}")
    with st.form(f"q{S.idx}"):
        choice = st.radio(q["question"], q["choices"], index=None)
        if not st.form_submit_button("Manaraka"):
            return
        if choice is None:
            st.warning("Mifidiana valiny aloha")
            return
        S.answers.append({"id": q["id"], "choice": q["choices"].index(choice)})
        S.idx += 1
        if S.idx >= len(S.questions):
            res = call("POST", "/submit", {"answers": S.answers})
            if not res:  # échec réseau : on reste sur la dernière question
                S.idx -= 1
                S.answers.pop()
                return
            S.result = res
        st.rerun()


def _result(S):
    render_result(S.result, S.by_id)
    if st.button("Averina"):
        state.reset_quiz()
        st.rerun()
