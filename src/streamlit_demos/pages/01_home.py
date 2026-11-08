"""Home page: welcome + the Streamlit "rerun" mental model.

Demonstrates: st.title, st.markdown, st.page_link, st.button, st.write, st.columns.
"""

import streamlit as st

st.title("🎈 Streamlit Showcase")
st.markdown(
    "Welcome! This app demonstrates **every major Streamlit feature**. "
    "Click around on each page, then open the matching file in `pages/` to "
    "see how it was built."
)

# ---------- 1. The one idea you must know ----------
st.header("How Streamlit works")
st.markdown(
    """
1. Your Python script runs **top to bottom**.
2. When you click, type or drag a widget, the **whole script runs again**.
3. A widget is just a function that **returns its current value**.
4. Variables are reset on every rerun, so use `st.session_state` or caching to remember things.
"""
)

# ---------- 2. See a rerun happen ----------
# TRY THIS: click the button several times. The script reruns each time, but
# the counter only survives because it is stored in st.session_state.
st.subheader("Watch a rerun")
if "home_clicks" not in st.session_state:
    st.session_state.home_clicks = 0  # runs only the first time

plain_counter = 0  # reset to 0 on EVERY rerun - that's the point

if st.button("Click me", key="home_button"):
    st.session_state.home_clicks += 1
    plain_counter += 1

col1, col2 = st.columns(2)
col1.metric("Counter in session_state (remembered)", st.session_state.home_clicks)
col2.metric("Plain variable (forgotten each rerun)", plain_counter)
st.caption("Idea: normal variables reset on every rerun; session_state persists.")

# ---------- 3. Links to other pages ----------
# st.page_link makes a clickable link to another page of this app.
# TRY THIS: click a link to jump to that page.
st.header("Where to next?")
st.page_link("pages/02_input_widgets.py", label="Input widgets", icon="🎛️")
st.page_link("pages/07_session_state.py", label="Session state", icon="🧠")
st.page_link("pages/10_data_charts.py", label="Data & charts", icon="📊")
