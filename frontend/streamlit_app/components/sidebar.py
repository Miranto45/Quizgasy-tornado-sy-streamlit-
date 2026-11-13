
import streamlit as st

import config
import state


def render():
    """Affiche la barre latérale et renvoie la page choisie (None si non connecté)."""
    st.sidebar.text_input("Serveur API", config.DEFAULT_API, key="api_url",
                          help="FastAPI = :8000 | Tornado = :8001")
    if not st.session_state.token:
        return None
    st.sidebar.write(f"Salama, **{st.session_state.username}**")
    page = st.sidebar.radio("Pejy", config.PAGES)
    if st.sidebar.button("Hivoaka"):
        state.logout()
        st.rerun()
    return page
