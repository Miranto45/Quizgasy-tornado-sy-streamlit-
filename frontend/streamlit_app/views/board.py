"""Page Laharana : classement + page live Tornado."""
import pandas as pd
import streamlit as st

import config
from api_client import call


def render():
    st.header("Laharana")
    rows = call("GET", "/leaderboard")
    if rows is None:
        return
    if not rows:
        st.info("Mbola tsy misy isa.")
    else:
        df = pd.DataFrame(rows).rename(columns={"username": "Mpilalao", "points": "Isa",
                                                "best": "Tsara indrindra", "games": "Lalao"})
        st.dataframe(df, hide_index=True, width="stretch")
        st.bar_chart(df.set_index("Mpilalao")["Isa"])
    with st.expander("Live (Tornado)"):
        st.iframe(config.LIVE_URL, height=480)
