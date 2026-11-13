"""Fanadinana Madagasikara - client web Streamlit
Lancer : streamlit run app.py     ->  http://localhost:8501
Marche avec le backend FastAPI (:8000) comme avec le backend Tornado (:8001).
"""
import streamlit as st

import state
from components import sidebar
from views import board, login, play, profile

st.set_page_config(page_title="Fanadinana Madagasikara", page_icon="🇲🇬")
state.init_state()

VIEWS = {"Lalao": play.render, "Laharana": board.render, "Mombamomba": profile.render}

page = sidebar.render()
if page is None:
    login.render()
else:
    VIEWS[page]()
