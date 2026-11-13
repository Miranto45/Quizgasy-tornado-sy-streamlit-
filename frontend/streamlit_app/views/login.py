
import streamlit as st

from api_client import call


def render():
    st.title("Fanadinana Madagasikara")
    st.caption("Hamarino ny fahalalanao ny Nosintsika")
    tab_in, tab_up = st.tabs(["Hiditra", "Hamorona kaonty"])
    for tab, path, label in ((tab_in, "/login", "Hiditra"), (tab_up, "/register", "Hamorona")):
        with tab, st.form(f"form{path}"):
            user = st.text_input("Anarana", key=f"user{path}")
            pwd = st.text_input("Teny miafina", type="password", key=f"pwd{path}")
            if st.form_submit_button(label):
                res = call("POST", path, {"username": user.strip(), "password": pwd})
                if res:
                    st.session_state.token, st.session_state.username = res["token"], res["username"]
                    st.rerun()
