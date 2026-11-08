# CLAUDE.md — Streamlit Showcase Project

Beginner-friendly, exhaustive Streamlit demo app. A learner runs `streamlit run app.py`, clicks through every major feature, then reads the code to understand it. Keep everything simple, flat and heavily commented.

## Commands

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py                                 # run the app
streamlit run app.py --server.headless true          # headless boot check
python -m py_compile app.py pages/*.py utils.py      # syntax check
pytest tests/ -q                                     # AppTest smoke tests
```

## Project structure

```
app.py                      # entrypoint: set_page_config, st.navigation (grouped), shared sidebar
pages/
  01_home.py                # welcome, rerun model, st.page_link
  02_input_widgets.py       # all input widgets + live values summary
  03_output_elements.py     # text, code, latex, badge, metric, json, alerts, toast, balloons
  04_status_progress.py     # progress, spinner, st.status, st.empty, long-task simulation
  05_layouts_containers.py  # columns, tabs, expander, popover, container, sidebar, dialog, divider
  06_forms.py               # st.form, submit button, clear_on_submit, validation
  07_session_state.py       # session_state, callbacks, keys, query_params
  08_caching.py             # cache_data (ttl), cache_resource, st.fragment, run_every
  09_chat.py                # chat_input, chat_message, write_stream (mock, no API key)
  10_data_charts.py         # dataframe, data_editor, bar/line/area/scatter charts, map, CSV upload
  11_media.py               # image, audio (generated WAV), video, camera_input, audio_input
  12_embeds_html_json.py    # st.html, iframe, json, code in several languages
data/sales.csv              # ~200 rows: date, region, product, units, revenue
utils.py                    # tiny shared helpers only
requirements.txt            # minimum versions pinned
.streamlit/config.toml      # commented theme example
README.md                   # quickstart
docs/EXPLORING_THE_CODE.md  # learning guide (also export .docx if python-docx available)
tests/test_pages.py         # AppTest smoke test per page
```

## Coding rules

- Use the **installed** Streamlit version's current APIs: `st.navigation` / `st.Page`, `st.pills`, `st.segmented_control`, `st.popover`, `st.status`, `st.toast`, `st.dialog`, `st.fragment`, `st.audio_input`, `st.feedback`, `st.badge`, `st.html`. Never use deprecated APIs (`st.experimental_*`, `st.cache`, `use_container_width` where superseded, etc.). If unsure an API exists, check the installed package before using it.
- Python 3.10+. Type hints only where they aid readability.
- Flat, simple code. Small functions with descriptive names. No classes unless unavoidable. No clever abstractions, decorators beyond Streamlit's, or metaprogramming.
- Every widget gets an explicit, unique `key=` when it is reused or read from `session_state`.
- No external API keys, network downloads or paid services. Generate sample data, images and audio in code (numpy / PIL). Video may use a public URL with a note on local files.
- Keep `utils.py` minimal; each page must be readable on its own.

## Comment and docstring rules (important)

- Every file starts with a module docstring: what the page demonstrates and which `st.*` functions it covers.
- Comment **why**, not just what. Assume the reader has never used Streamlit.
- Put a `# TRY THIS:` comment above each demo telling the learner what to click or change.
- Each demo shows the widget, its returned value (via `st.write`, `st.json` or `st.code`) and the idea in one line, so learners see input -> output.
- Use section banners in code, e.g. `# ---------- 1. Buttons ----------`.

## Docs rules

`docs/EXPLORING_THE_CODE.md` must contain:
1. Mental model: script reruns top-to-bottom on every interaction; widgets return values; session_state and caching manage reruns.
2. Suggested learning path: page order with a 15-minute exercise per page.
3. Table mapping every feature -> file -> section.
4. "Break it and see" experiments (remove a key, move code in/out of a form, change ttl).
5. Common beginner mistakes and fixes.
6. Next steps: Community Cloud deployment, `st.secrets`, `st.connection`, `AppTest`.

## Feature checklist (all must be demonstrated)

button, download_button, link_button, checkbox, toggle, radio, selectbox, multiselect, slider, select_slider, number_input, date_input, time_input, text_input, text_area, color_picker, pills, segmented_control, feedback, file_uploader, progress, spinner, status, toast, empty, columns, tabs, expander, popover, container, sidebar, multipage navigation, divider, dialog, forms, session_state, query_params, cache_data, cache_resource, fragment, chat_input / chat_message / write_stream, dataframe, data_editor, table, metric, bar / line / area / scatter charts, map, CSV upload, image, audio, video, camera_input, audio_input, html, iframe, json, code, latex, markdown.

## Workflow

1. **Plan first**: reply with a short plan (file list, feature -> page mapping, any API you are unsure about), then proceed without waiting unless something is ambiguous.
2. Build page by page; keep each file self-contained and runnable.
3. **Verify before claiming done**:
   - `python -m py_compile` on all `.py` files
   - `pytest tests/` (AppTest loads each page and asserts no exception)
   - headless boot of `app.py` with no errors in the log
4. Finish with the feature checklist, each item marked with the file where it is demonstrated.
5. If a check fails, fix the root cause; do not delete or weaken tests to pass.

## Do not

- Do not add dependencies beyond: streamlit, pandas, numpy, pillow, pytest (plus python-docx only for the optional .docx export).
- Do not put secrets, API keys or real personal data in any file.
- Do not restructure the folder layout above without asking.
- Do not write long files in one shot; build in stages and run after each page.
