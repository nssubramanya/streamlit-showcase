"""Output elements: ways to DISPLAY things on the page.

Demonstrates: st.title/header/subheader, st.markdown, st.text, st.caption,
st.code, st.latex, st.badge, st.metric, st.json, st.success/info/warning/
error/exception, st.toast, st.balloons, st.snow, st.write.

Unlike input widgets, these just show information and return nothing useful.
"""

import streamlit as st

st.title("📝 Output elements")

# ---------- 1. Text ----------
st.header("1. Text")

# TRY THIS: edit the strings below and watch the page update after saving.
st.subheader("A subheader")
st.markdown("**Bold**, *italic*, `inline code`, ~~strikethrough~~ and [a link](https://streamlit.io).")
st.markdown("Colours: :red[red] :green[green] :blue[blue] and emoji :tada:")
st.text("st.text shows fixed-width plain text, no formatting.")
st.caption("st.caption is small, greyed-out text - good for hints.")
st.write("st.write is the Swiss-army knife: it accepts text, numbers, dicts, DataFrames...")
st.write({"any": "dict", "works": [1, 2, 3]})
st.caption("Idea: use st.write when you are not sure which element to pick.")

# ---------- 2. Code and maths ----------
st.header("2. Code and maths")

# TRY THIS: change the language argument to "javascript" and look at the colours.
st.code("def greet(name):\n    return f'Hello, {name}!'", language="python")
st.latex(r"E = mc^2 \quad\text{and}\quad \sum_{i=1}^{n} i = \frac{n(n+1)}{2}")
st.caption("Idea: st.code adds syntax highlighting and a copy button; st.latex renders formulas.")

# ---------- 3. Badges ----------
st.header("3. Badges")

# TRY THIS: change color to "red", "orange", "yellow", "blue", "violet", "gray".
st.badge("New", icon=":material/star:", color="green")
st.badge("Beta", color="orange")
st.markdown("Badges also work inline: :blue-badge[Info] :red-badge[Alert]")

# ---------- 4. Metrics ----------
st.header("4. Metrics")

# TRY THIS: change the delta to a negative number and the arrow turns red.
col_a, col_b, col_c = st.columns(3)
col_a.metric("Temperature", "21 °C", "1.2 °C")
col_b.metric("Users", "1,204", "-37")
col_c.metric("Errors", "3", "-2", delta_color="inverse")  # inverse: down is good
st.caption("Idea: metric = big number + coloured change. delta_color flips the meaning.")

# ---------- 5. JSON ----------
st.header("5. JSON")

# TRY THIS: click the little arrows to collapse and expand the tree.
st.json({"name": "Ada", "skills": ["maths", "code"], "address": {"city": "London", "zip": "N1"}})

# ---------- 6. Alerts ----------
st.header("6. Status messages")

st.success("Success: it worked.")
st.info("Info: something helpful to know.")
st.warning("Warning: be careful here.")
st.error("Error: something went wrong.")
# TRY THIS: click to see how st.exception displays a Python error with its traceback.
if st.button("Show an exception", key="out_exception"):
    try:
        1 / 0  # deliberately fail so we can show st.exception
    except ZeroDivisionError as err:
        st.exception(err)
st.caption("Idea: pick the colour that matches the meaning of the message.")

# ---------- 7. Toast and celebrations ----------
st.header("7. Toast and celebrations")

# TRY THIS: click each button. A toast pops up in the corner and fades away.
if st.button("Show a toast", key="out_toast"):
    st.toast("Saved successfully!", icon="✅")
if st.button("Balloons!", key="out_balloons"):
    st.balloons()
if st.button("Snow!", key="out_snow"):
    st.snow()
st.caption("Idea: toasts are non-blocking notifications; balloons/snow are just for fun.")
