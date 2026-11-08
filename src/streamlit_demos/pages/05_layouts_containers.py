"""Layouts & containers: arrange elements on the page.

Demonstrates: st.columns, st.tabs, st.expander, st.popover, st.container,
st.sidebar, st.dialog, st.divider.
"""

import streamlit as st

st.title("🧱 Layouts & containers")

# ---------- 1. Columns ----------
st.header("1. Columns")

# TRY THIS: change [1, 2] to [1, 1, 1] (and add a third column) to resize them.
left, right = st.columns([1, 2])  # numbers = relative widths
left.write("I am the narrow column.")
with right:  # `with` is another way to put things inside
    st.write("I am the wide column (twice as wide).")
    st.button("A button inside a column", key="lay_col_button")
st.caption("Idea: use `col.write(...)` or `with col:` - both put content in that column.")

st.divider()  # a thin horizontal line

# ---------- 2. Tabs ----------
st.header("2. Tabs")

# TRY THIS: click each tab. All tabs run on every rerun; they only hide content.
tab_one, tab_two = st.tabs(["📈 First", "📉 Second"])
with tab_one:
    st.write("Content of the first tab.")
with tab_two:
    st.write("Content of the second tab.")

st.divider()

# ---------- 3. Expander and popover ----------
st.header("3. Expander and popover")

# TRY THIS: click the expander title to open it.
with st.expander("Click to expand", expanded=False):
    st.write("Hidden details live here. Great for long explanations.")

# TRY THIS: click the popover button; it floats above the page.
with st.popover("Open popover"):
    st.write("I float over the page.")
    name = st.text_input("Your name", key="lay_popover_name")
    st.write(f"Hello, {name or 'stranger'}!")
st.caption("Idea: an expander pushes content down; a popover overlays it.")

st.divider()

# ---------- 4. Container ----------
st.header("4. Container")

# A container is a spot you can fill later, in any order.
box = st.container(border=True)
st.write("This line is written AFTER the container but appears below it.")
box.write("This line was added to the container later in the code, yet shows first.")
st.caption("Idea: containers let you write to an earlier spot on the page.")

st.divider()

# ---------- 5. Sidebar ----------
st.header("5. Sidebar")

# TRY THIS: look at the sidebar on the left - the slider below lives there.
st.sidebar.subheader("Sidebar of this page")
sidebar_value = st.sidebar.slider("A sidebar slider", 0, 10, 5, key="lay_sidebar_slider")
st.write("Sidebar slider value:", sidebar_value)
st.caption("Idea: `st.sidebar.<widget>` or `with st.sidebar:` puts widgets in the sidebar.")

st.divider()


# ---------- 6. Dialog ----------
st.header("6. Dialog (modal window)")


# @st.dialog turns a function into a modal pop-up.
@st.dialog("Please confirm")
def confirm_dialog():
    st.write("Do you really want to do this?")
    if st.button("Yes, do it", key="lay_dialog_yes"):
        st.session_state.dialog_result = "You confirmed!"
        st.rerun()  # close the dialog and refresh the page


# TRY THIS: open the dialog and click the button inside it.
if st.button("Open dialog", key="lay_dialog_open"):
    confirm_dialog()
st.write("Dialog result:", st.session_state.get("dialog_result", "(nothing yet)"))
st.caption("Idea: call the decorated function to open it; st.rerun() closes it.")
