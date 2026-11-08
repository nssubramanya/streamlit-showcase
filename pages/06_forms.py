"""Forms: collect several inputs and process them with ONE click.

Demonstrates: st.form, st.form_submit_button, clear_on_submit, simple
validation with st.error / st.success.

Normally every widget change reruns the script. Inside a form, nothing
reruns until the submit button is pressed.
"""

import streamlit as st

st.title("📋 Forms")

# ---------- 1. A basic form ----------
st.header("1. A basic form")

# TRY THIS: change the fields. Notice the page does NOT rerun until you submit.
with st.form("profile_form"):
    name = st.text_input("Name", key="form_name")
    age = st.number_input("Age", 0, 120, 30, key="form_age")
    colour = st.selectbox("Favourite colour", ["Red", "Green", "Blue"], key="form_colour")
    submitted = st.form_submit_button("Submit")  # required inside every form

if submitted:
    st.write("Submitted values:")
    st.json({"name": name, "age": age, "colour": colour})
st.caption("Idea: the form_submit_button returns True only on the run after you click it.")

# ---------- 2. Validation ----------
st.header("2. Validation")

# TRY THIS: submit with an empty name, then with a bad email, then with valid data.
with st.form("signup_form"):
    signup_name = st.text_input("Name *", key="signup_name")
    email = st.text_input("Email *", key="signup_email")
    accepted = st.checkbox("I accept the terms", key="signup_terms")
    signup_clicked = st.form_submit_button("Sign up")

if signup_clicked:
    errors = []
    if not signup_name.strip():
        errors.append("Name is required.")
    if "@" not in email:
        errors.append("Email must contain '@'.")
    if not accepted:
        errors.append("You must accept the terms.")
    if errors:
        for message in errors:
            st.error(message)
    else:
        st.success(f"Welcome, {signup_name}!")
st.caption("Idea: validate AFTER submit; show errors, or success when the list is empty.")

# ---------- 3. clear_on_submit ----------
st.header("3. Clearing the form after submit")

if "notes" not in st.session_state:
    st.session_state.notes = []  # remember notes across reruns

# TRY THIS: add a note. The text box empties itself, the note stays in the list.
with st.form("notes_form", clear_on_submit=True):
    note = st.text_input("New note", key="form_note")
    add_clicked = st.form_submit_button("Add note")

if add_clicked and note:
    st.session_state.notes.append(note)
st.write("Saved notes:", st.session_state.notes)
st.caption("Idea: clear_on_submit=True resets the widgets; session_state keeps the results.")

# ---------- 4. Form vs no form ----------
st.header("4. Same widget, with and without a form")

col_form, col_live = st.columns(2)
with col_form:
    # TRY THIS: drag this slider - the text below does not change until you submit.
    with st.form("compare_form"):
        in_form = st.slider("Inside a form", 0, 100, 50, key="form_slider_in")
        st.form_submit_button("Apply")
    st.write("Value used:", in_form)
with col_live:
    # TRY THIS: drag this slider - the text updates immediately.
    live = st.slider("Outside a form", 0, 100, 50, key="form_slider_out")
    st.write("Value used:", live)
st.caption("Idea: forms batch up changes so the app does not rerun on every tweak.")
