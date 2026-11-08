"""Session state: make the app REMEMBER things between reruns.

Demonstrates: st.session_state (read/write), widget keys, on_click and
on_change callbacks, st.query_params (state stored in the page URL).
"""

import streamlit as st

st.title("🧠 Session state")
st.write(
    "Every rerun resets normal Python variables. `st.session_state` is a "
    "dictionary that survives reruns (one per browser tab)."
)

# ---------- 1. A counter ----------
st.header("1. A counter")

# Create the key ONCE. Without the `if`, the counter would reset every run.
if "counter" not in st.session_state:
    st.session_state.counter = 0

# TRY THIS: click both buttons. Then refresh the browser - the counter resets
# because a refresh starts a brand-new session.
col_plus, col_minus, col_reset = st.columns(3)
if col_plus.button("➕ Add", key="ss_add"):
    st.session_state.counter += 1
if col_minus.button("➖ Subtract", key="ss_sub"):
    st.session_state.counter -= 1
if col_reset.button("Reset", key="ss_reset"):
    st.session_state.counter = 0
st.metric("Counter", st.session_state.counter)
st.caption("Idea: check `if key not in st.session_state` to set an initial value once.")

# ---------- 2. Widget keys ----------
st.header("2. Widget keys")

# A widget with key="ss_name" automatically stores its value in
# st.session_state["ss_name"], so you can read OR set it from anywhere.
# TRY THIS: type a name, then press the "Fill in 'Ada'" button.
st.text_input("Your name", key="ss_name")
st.write("Read from session_state:", st.session_state.ss_name)


def fill_in_ada():
    # Callbacks run BEFORE the rerun, which is the only time you may
    # change a widget's value from code.
    st.session_state.ss_name = "Ada"


st.button("Fill in 'Ada'", on_click=fill_in_ada, key="ss_fill")
st.caption("Idea: setting a widget's key in a callback changes what the widget shows.")

# ---------- 3. Callbacks ----------
st.header("3. Callbacks")

if "change_log" not in st.session_state:
    st.session_state.change_log = []


def log_change():
    # on_change runs when the widget value changes, before the page reruns.
    st.session_state.change_log.append(f"Slider moved to {st.session_state.ss_slider}")


# TRY THIS: move the slider a few times and watch the log grow.
st.slider("Slider with on_change", 0, 10, 5, key="ss_slider", on_change=log_change)
st.write("Change log:", st.session_state.change_log[-5:])  # show the last five
st.button("Clear log", on_click=lambda: st.session_state.change_log.clear(), key="ss_clear_log")
st.caption("Idea: callbacks are the clean way to react to a click or change.")

# ---------- 4. Inspect everything ----------
st.header("4. See all session state")

# TRY THIS: interact with other widgets above and watch this update.
st.json({key: str(value) for key, value in st.session_state.items()})

# ---------- 5. Query params ----------
st.header("5. Query params (state in the URL)")

# st.query_params behaves like a dict tied to the ?key=value part of the URL.
# TRY THIS: click the button, then look at the browser address bar. Copy that
# URL into a new tab and the value is still there - great for sharing.
current_topic = st.query_params.get("topic", "none")
st.write("Current `?topic=` value:", current_topic)

col_a, col_b, col_c = st.columns(3)
if col_a.button("topic=cats", key="qp_cats"):
    st.query_params["topic"] = "cats"
    st.rerun()  # rerun so the line above shows the new value
if col_b.button("topic=dogs", key="qp_dogs"):
    st.query_params["topic"] = "dogs"
    st.rerun()
if col_c.button("Clear", key="qp_clear"):
    st.query_params.clear()
    st.rerun()
st.caption("Idea: query_params let users bookmark or share the exact state of your app.")
