"""Status & progress: tell the user that something is happening.

Demonstrates: st.progress, st.spinner, st.status, st.empty, and a simulated
long-running task (time.sleep stands in for slow work).
"""

import time

import streamlit as st

st.title("⏳ Status & progress")

# ---------- 1. Progress bar ----------
st.header("1. Progress bar")

# TRY THIS: click the button and watch the bar fill up.
if st.button("Run progress bar", key="prog_button"):
    bar = st.progress(0, text="Starting...")
    for percent in range(0, 101, 10):
        time.sleep(0.05)  # pretend to work
        bar.progress(percent, text=f"Working... {percent}%")  # update the SAME bar
    bar.empty()  # remove the bar when finished
    st.success("Done!")
st.caption("Idea: st.progress returns an object; call .progress() on it to update in place.")

# ---------- 2. Spinner ----------
st.header("2. Spinner")

# TRY THIS: click and see the spinner while the `with` block is running.
if st.button("Run spinner", key="spin_button"):
    with st.spinner("Thinking hard..."):
        time.sleep(1.5)
    st.success("Spinner finished.")
st.caption("Idea: the spinner shows for exactly as long as the `with` block runs.")

# ---------- 3. Status container ----------
st.header("3. Status container")

# TRY THIS: click and expand the status box to see the log lines.
if st.button("Run status", key="status_button"):
    with st.status("Processing data...", expanded=True) as status:
        st.write("Loading file...")
        time.sleep(0.5)
        st.write("Cleaning rows...")
        time.sleep(0.5)
        st.write("Saving results...")
        time.sleep(0.5)
        status.update(label="All steps complete!", state="complete", expanded=False)
st.caption("Idea: st.status is a spinner that also keeps a log; update() sets the final state.")

# ---------- 4. Empty placeholder ----------
st.header("4. st.empty (a replaceable slot)")

# TRY THIS: click and watch one slot change text, then disappear.
if st.button("Run countdown", key="empty_button"):
    slot = st.empty()  # reserves one spot on the page
    for seconds_left in [3, 2, 1]:
        slot.write(f"⏱️ {seconds_left}...")  # each write REPLACES the previous
        time.sleep(0.5)
    slot.success("Liftoff! 🚀")
st.caption("Idea: st.empty gives you one element you can overwrite or clear later.")

# ---------- 5. Long task simulation ----------
st.header("5. Putting it together: a long task")

# TRY THIS: change the number of steps, then click Start.
steps = st.slider("Number of steps", 3, 15, 6, key="long_steps")
if st.button("Start long task", key="long_button"):
    bar = st.progress(0)
    log = st.empty()
    for i in range(1, steps + 1):
        log.info(f"Step {i} of {steps}")
        bar.progress(i / steps)  # a float between 0.0 and 1.0 also works
        time.sleep(0.2)
    log.success(f"Finished all {steps} steps.")
st.caption("Idea: combine a progress bar with an st.empty message for friendly feedback.")
