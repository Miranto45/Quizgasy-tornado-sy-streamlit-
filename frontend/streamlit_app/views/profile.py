
import streamlit as st

from api_client import call


def render():
    st.header("Mombamomba")
    me = call("GET", "/me")
    if me:
        a, b, c = st.columns(3)
        a.metric("Lalao", me["games"])
        b.metric("Isa tsara indrindra", me["best"])
        c.metric("Isa rehetra", me["points"])
