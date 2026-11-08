"""Caching & fragments: make the app fast and avoid needless reruns.

Demonstrates: st.cache_data (with ttl), st.cache_resource, st.fragment,
st.fragment(run_every=...), and st.rerun.

Because the script reruns on every click, slow work (loading data, opening a
connection) would repeat each time. Caching remembers the result instead.
"""

import time
from datetime import datetime

import streamlit as st

st.title("⚡ Caching & fragments")

# ---------- 1. cache_data ----------
st.header("1. st.cache_data (remember function results)")


@st.cache_data
def slow_square(number: int) -> int:
    # Pretend this is a slow database query or calculation.
    time.sleep(1.5)
    return number * number


# TRY THIS: pick 4 (slow the first time), then pick 5, then 4 again (instant!).
chosen = st.number_input("Number to square", 0, 100, 4, key="cache_number")
start = time.time()
result = slow_square(chosen)
st.write({"input": chosen, "result": result, "seconds_taken": round(time.time() - start, 2)})
st.caption("Idea: same inputs -> cached answer. Different inputs -> the function runs again.")

# TRY THIS: click to wipe the cache, then pick 4 again - it is slow once more.
if st.button("Clear cache_data", key="cache_clear"):
    st.cache_data.clear()
    st.rerun()

# ---------- 2. cache_data with ttl ----------
st.header("2. ttl (time to live)")


@st.cache_data(ttl=5)  # forget the answer after 5 seconds
def current_time_cached() -> str:
    return datetime.now().strftime("%H:%M:%S")


# TRY THIS: click "Rerun" repeatedly. The time stays the same for 5 seconds,
# then jumps. Change ttl=5 to ttl=1 or ttl=30 and see the difference.
st.write("Cached time:", current_time_cached())
st.write("Real time:  ", datetime.now().strftime("%H:%M:%S"))
st.button("Rerun", key="cache_rerun")
st.caption("Idea: ttl keeps data fresh enough without hitting the slow source every time.")

# ---------- 3. cache_resource ----------
st.header("3. st.cache_resource (share one object)")


@st.cache_resource
def get_fake_connection() -> dict:
    # Use cache_resource for things you can't copy: DB connections, ML models.
    # The SAME object is returned to every user and every rerun.
    return {"opened_at": datetime.now().strftime("%H:%M:%S"), "id": id(object())}


# TRY THIS: click Rerun above several times; opened_at never changes.
st.write("Shared connection object:", get_fake_connection())
st.caption("Idea: cache_data stores a COPY of data; cache_resource stores the object itself.")

# ---------- 4. Fragments ----------
st.header("4. st.fragment (rerun only part of the page)")


@st.fragment
def fragment_counter():
    # Clicking inside a fragment reruns ONLY this function, not the whole page.
    if "frag_count" not in st.session_state:
        st.session_state.frag_count = 0
    if st.button("Increase (fragment only)", key="frag_button"):
        st.session_state.frag_count += 1
    st.write("Fragment count:", st.session_state.frag_count)
    st.write("Fragment last ran at:", datetime.now().strftime("%H:%M:%S.%f")[:-3])


# TRY THIS: click the fragment button. Its time changes but the 'Page ran at'
# line below does not, proving the rest of the page was NOT rerun.
fragment_counter()
st.write("Page ran at:", datetime.now().strftime("%H:%M:%S.%f")[:-3])
st.caption("Idea: fragments make big apps feel snappy by limiting what reruns.")

# ---------- 5. Auto-refreshing fragment ----------
st.header("5. run_every (auto refresh)")


@st.fragment(run_every="2s")  # rerun this function every 2 seconds by itself
def live_clock():
    st.metric("Live clock", datetime.now().strftime("%H:%M:%S"))


# TRY THIS: just watch - the clock ticks without any clicking.
live_clock()
st.caption("Idea: run_every is perfect for dashboards that poll for new data.")
