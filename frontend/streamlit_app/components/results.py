
import streamlit as st


def render_result(result: dict, by_id: dict):
    st.metric("Isa", f"{result['score']} / {result['total']}")
    wrong = [d for d in result["details"] if not d["correct"]]
    if not wrong:
        st.success("Tsara be! Marina daholo ny valinao!")
    for d in wrong:
        q = by_id[d["id"]]
        with st.expander(q["question"]):
            st.write(f"Valiny marina: **{q['choices'][d['correct_index']]}**")
            st.caption(d["explanation"])
