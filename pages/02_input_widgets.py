"""Input widgets: every common way a user can give the app a value.

Demonstrates: st.button, st.download_button, st.link_button, st.checkbox,
st.toggle, st.radio, st.selectbox, st.multiselect, st.slider,
st.select_slider, st.number_input, st.date_input, st.time_input,
st.text_input, st.text_area, st.color_picker, st.pills,
st.segmented_control, st.feedback, st.file_uploader.

Remember: a widget is a function that RETURNS its current value.
"""

import datetime

import streamlit as st

st.title("🎛️ Input widgets")
st.caption("Each demo shows the widget, the value it returns, and the idea.")

# ---------- 1. Buttons ----------
st.header("1. Buttons")

# TRY THIS: click the button. It returns True for ONE rerun only, then False.
clicked = st.button("Click me", key="w_button")
st.write("`st.button` returned:", clicked)
st.caption("Idea: a button is True only on the run right after the click.")

# TRY THIS: click to save a small text file from the browser.
st.download_button(
    "Download a text file",
    data="Hello from Streamlit!\n",
    file_name="hello.txt",
    mime="text/plain",
    key="w_download",
)
st.caption("Idea: download_button hands Python data to the user as a file.")

# link_button just opens a URL in a new tab; it returns nothing useful.
st.link_button("Open Streamlit website", "https://streamlit.io")

# ---------- 2. Boolean and choice widgets ----------
st.header("2. Checkbox, toggle and choices")

# TRY THIS: tick the box and flip the toggle.
agree = st.checkbox("I like Streamlit", key="w_checkbox")
dark = st.toggle("Fancy mode", key="w_toggle")
st.write({"checkbox": agree, "toggle": dark})
st.caption("Idea: checkbox and toggle return True/False.")

# TRY THIS: pick a different option in each widget.
radio_value = st.radio("Radio (pick one)", ["Red", "Green", "Blue"], key="w_radio")
select_value = st.selectbox("Selectbox (dropdown)", ["Cat", "Dog", "Bird"], key="w_select")
multi_value = st.multiselect(
    "Multiselect (pick many)", ["Python", "SQL", "Rust", "Go"], default=["Python"], key="w_multi"
)
st.write({"radio": radio_value, "selectbox": select_value, "multiselect": multi_value})
st.caption("Idea: single-choice widgets return one value, multiselect returns a list.")

# pills and segmented_control are modern, compact alternatives.
# TRY THIS: click several pills; segmented_control allows only one by default.
pills_value = st.pills(
    "Pills (multi)", ["Easy", "Fast", "Pretty"], selection_mode="multi", key="w_pills"
)
segment_value = st.segmented_control(
    "Segmented control", ["Day", "Week", "Month"], default="Week", key="w_segment"
)
st.write({"pills": pills_value, "segmented_control": segment_value})
st.caption("Idea: pills with selection_mode='multi' return a list; otherwise one value or None.")

# ---------- 3. Numbers ----------
st.header("3. Sliders and numbers")

# TRY THIS: drag the sliders; pass a tuple as the value to get a range slider.
slider_value = st.slider("Slider", min_value=0, max_value=100, value=25, key="w_slider")
range_value = st.slider("Range slider", 0, 100, (20, 80), key="w_range")
size_value = st.select_slider(
    "Select slider (named steps)", options=["S", "M", "L", "XL"], value="M", key="w_select_slider"
)
number_value = st.number_input(
    "Number input", min_value=0.0, max_value=10.0, value=1.5, step=0.5, key="w_number"
)
st.write(
    {"slider": slider_value, "range": range_value, "select_slider": size_value, "number": number_value}
)
st.caption("Idea: a range slider returns a (low, high) tuple.")

# ---------- 4. Dates and times ----------
st.header("4. Date and time")

# TRY THIS: open the calendar and choose a day.
date_value = st.date_input("Date input", datetime.date(2025, 1, 1), key="w_date")
time_value = st.time_input("Time input", datetime.time(9, 30), key="w_time")
st.write({"date": str(date_value), "time": str(time_value)})
st.caption("Idea: these return datetime.date / datetime.time objects.")

# ---------- 5. Text ----------
st.header("5. Text and colour")

# TRY THIS: type something and press Enter (or click outside the box).
text_value = st.text_input("Text input", placeholder="Your name", key="w_text")
area_value = st.text_area("Text area (multi-line)", key="w_area")
password_value = st.text_input("Password (hidden)", type="password", key="w_password")
color_value = st.color_picker("Colour picker", "#FF4B4B", key="w_color")
st.write(
    {
        "text": text_value,
        "text_area": area_value,
        "password_length": len(password_value),  # never display a real password
        "color": color_value,
    }
)
st.caption("Idea: text widgets update when you press Enter or click away.")

# ---------- 6. Feedback ----------
st.header("6. Feedback")

# TRY THIS: click a star. Options are "thumbs", "faces" or "stars".
stars = st.feedback("stars", key="w_feedback")
st.write("`st.feedback` returned (0-4, or None):", stars)
st.caption("Idea: the value is a zero-based index, so 5 stars -> 4.")

# ---------- 7. File upload ----------
st.header("7. File uploader")

# TRY THIS: upload any small text file.
uploaded = st.file_uploader("Upload a text file", type=["txt", "md", "csv"], key="w_upload")
if uploaded is not None:
    st.write({"name": uploaded.name, "size_bytes": uploaded.size, "type": uploaded.type})
    st.code(uploaded.getvalue().decode("utf-8", errors="replace")[:500])
else:
    st.info("Nothing uploaded yet - the widget returns None until you pick a file.")
st.caption("Idea: the uploader returns None, or a file-like object you can read.")
