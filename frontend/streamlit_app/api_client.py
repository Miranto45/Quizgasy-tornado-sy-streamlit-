
import requests
import streamlit as st


def call(method: str, path: str, body=None):
    """Renvoie le JSON, ou None (après avoir affiché l'erreur) si la requête échoue."""
    S = st.session_state
    headers = {"Authorization": f"Bearer {S.token}"} if S.token else {}
    try:
        r = requests.request(method, S.api_url.rstrip("/") + path, json=body, headers=headers, timeout=8)
    except requests.RequestException:
        st.error("Tsy afaka mifandray amin'ny serveur")
        return None
    try:
        data = r.json()
    except ValueError:
        data = {}
    if r.status_code >= 400:
        detail = data.get("detail") if isinstance(data, dict) else None
        st.error(detail if isinstance(detail, str) else "Misy olana (hamarino ny fenoina)")
        return None
    return data
