"""Entrypoint of the Streamlit showcase app.  Run it with:  streamlit run app.py

Demonstrates: st.set_page_config, st.navigation, st.Page (grouped multipage
navigation) and a sidebar that is shared by every page.

How it works: this file runs FIRST on every rerun.  It declares the pages,
draws anything shared (the sidebar), then calls pg.run() to run the page the
user picked.
"""

import streamlit as st

# set_page_config must be the first Streamlit call, and only called once here.
st.set_page_config(page_title="Streamlit Showcase", page_icon="🎈", layout="wide")

# ---------- 1. Declare the pages (grouped into sections) ----------
# A dict maps "section title" -> list of pages. Sections show up as headings
# in the sidebar navigation.
pages = {
    "Start": [
        st.Page("pages/01_home.py", title="Home", icon="🏠", default=True),
    ],
    "Widgets & Output": [
        st.Page("pages/02_input_widgets.py", title="Input widgets", icon="🎛️"),
        st.Page("pages/03_output_elements.py", title="Output elements", icon="📝"),
        st.Page("pages/04_status_progress.py", title="Status & progress", icon="⏳"),
    ],
    "Structure & State": [
        st.Page("pages/05_layouts_containers.py", title="Layouts & containers", icon="🧱"),
        st.Page("pages/06_forms.py", title="Forms", icon="📋"),
        st.Page("pages/07_session_state.py", title="Session state", icon="🧠"),
        st.Page("pages/08_caching.py", title="Caching & fragments", icon="⚡"),
    ],
    "Apps & Data": [
        st.Page("pages/09_chat.py", title="Chat", icon="💬"),
        st.Page("pages/10_data_charts.py", title="Data & charts", icon="📊"),
        st.Page("pages/11_media.py", title="Media", icon="🖼️"),
        st.Page("pages/12_embeds_html_json.py", title="Embeds, HTML & code", icon="🧩"),
    ],
}
pg = st.navigation(pages)

# ---------- 2. Shared sidebar ----------
# Anything drawn here appears on every page, above/below the navigation.
st.sidebar.markdown("### 🎈 Streamlit Showcase")
st.sidebar.caption("Click through the pages, then read the code of each one.")
st.sidebar.link_button("Streamlit docs", "https://docs.streamlit.io")
st.sidebar.caption(f"Streamlit version: {st.__version__}")

# ---------- 3. Run the selected page ----------
pg.run()
