"""Embeds, HTML, JSON & code: show custom content and source code.

Demonstrates: st.html, st.iframe, st.json, st.code (several languages),
st.markdown, st.latex.
"""

import streamlit as st

st.title("🧩 Embeds, HTML & code")

# ---------- 1. Raw HTML ----------
st.header("1. st.html")

# TRY THIS: change the colour or the text and save the file.
st.html(
    """
    <div style="padding:16px;border-radius:8px;background:#e8f0fe;color:#1a3c8f">
        <b>Hello from raw HTML!</b> Use this for small custom snippets.
    </div>
    """
)
st.caption("Idea: st.html renders HTML and CSS (scripts are blocked for safety).")

# ---------- 2. Iframe ----------
st.header("2. st.iframe")

# TRY THIS: the iframe shows a whole web page inside yours. It needs internet,
# and some sites refuse to be embedded.
st.iframe("https://docs.streamlit.io", height=300)
st.caption("Idea: st.iframe embeds another page by URL.")

# ---------- 3. JSON ----------
st.header("3. st.json")

data = {"user": "ada", "scores": [9, 8, 10], "profile": {"active": True, "level": 3}}
# TRY THIS: set expanded=False (or a number like 1) to control how open the tree is.
st.json(data, expanded=True)
st.caption("Idea: st.json draws dictionaries and lists as a collapsible tree.")

# ---------- 4. Code in several languages ----------
st.header("4. st.code in several languages")

# TRY THIS: pick a language; the highlighting follows.
samples = {
    "python": "for i in range(3):\n    print('hi', i)",
    "javascript": "const add = (a, b) => a + b;\nconsole.log(add(1, 2));",
    "sql": "SELECT region, SUM(revenue)\nFROM sales\nGROUP BY region;",
    "bash": "pip install streamlit\nstreamlit run app.py",
    "json": '{"hello": "world", "numbers": [1, 2, 3]}',
}
language = st.segmented_control(
    "Language", list(samples), default="python", key="embed_language"
)
if language:  # the control returns None if the user un-clicks it
    st.code(samples[language], language=language, line_numbers=True)
st.caption("Idea: the `language` argument only changes colours; it never runs the code.")

# ---------- 5. Markdown and LaTeX ----------
st.header("5. Markdown and LaTeX")

# TRY THIS: edit the text area and see the preview update on Enter / click away.
source = st.text_area(
    "Write Markdown",
    "# Title\n- item one\n- item two\n\n**bold** and `code`",
    key="embed_markdown",
)
st.markdown(source)
st.latex(r"\int_0^1 x^2\,dx = \frac{1}{3}")
st.caption("Idea: st.markdown turns text with simple symbols into formatted output.")
