# Exploring the code

A guide for learning Streamlit by clicking through this app and then reading the code behind each page.

## 1. Mental model

1. **The script reruns top to bottom on every interaction.** Click a button, drag a slider or type in a box and Streamlit runs your Python file again from line 1.
2. **Widgets return values.** `age = st.slider("Age", 0, 100)` gives you the slider's current number as a normal Python variable.
3. **Normal variables reset on every rerun.** Anything you want to remember needs help:
   - `st.session_state` remembers values per browser tab (page 07).
   - `st.cache_data` / `st.cache_resource` remember results of slow functions across reruns and users (page 08).
   - `st.form` and `st.fragment` limit *what* reruns (pages 06 and 08).

`app.py` is the entrypoint. It declares the pages with `st.navigation`, draws the shared sidebar, then runs the selected page.

## 2. Suggested learning path (about 15 minutes per page)

| # | Page | 15-minute exercise |
|---|------|--------------------|
| 01 | Home | Click the button 5 times and compare the two counters. Then explain, in one sentence, why they differ. |
| 02 | Input widgets | For three widgets, change the `value=` or `options=` argument, save, and see what changes. Add a new `st.radio` with your own options. |
| 03 | Output elements | Add a fourth `st.metric` column. Change a `st.badge` colour. Write your own `st.latex` formula. |
| 04 | Status & progress | Make the progress bar take about 5 seconds. Add a fourth step to the `st.status` log. |
| 05 | Layouts & containers | Turn the 2 columns into 3. Move the popover inside a tab. Add a text input to the dialog. |
| 06 | Forms | Add a "phone number" field with validation (digits only). Add a second submit button. |
| 07 | Session state | Add a "Double" button to the counter. Add a third query-param button, then share the URL. |
| 08 | Caching & fragments | Change `ttl=5` to `ttl=1`, then `ttl=30`. Add a second fragment with its own button. |
| 09 | Chat | Change the mock bot so it reverses the user's message. Add a "Bot is typing" spinner. |
| 10 | Data & charts | Add a product filter next to the region filter. Chart `units` instead of `revenue`. |
| 11 | Media | Add a second generated image (try a checkerboard). Add a pitch of 1000 Hz. |
| 12 | Embeds, HTML & code | Add a new language sample to `st.code`. Style the `st.html` box differently. |

## 3. Feature to file to section

| Feature | File | Section |
|---|---|---|
| button, download_button, link_button | `pages/02_input_widgets.py` | 1. Buttons |
| checkbox, toggle, radio, selectbox, multiselect, pills, segmented_control | `pages/02_input_widgets.py` | 2. Checkbox, toggle and choices |
| slider, select_slider, number_input | `pages/02_input_widgets.py` | 3. Sliders and numbers |
| date_input, time_input | `pages/02_input_widgets.py` | 4. Date and time |
| text_input, text_area, color_picker | `pages/02_input_widgets.py` | 5. Text and colour |
| feedback | `pages/02_input_widgets.py` | 6. Feedback |
| file_uploader | `pages/02_input_widgets.py` | 7. File uploader |
| markdown, latex, code | `pages/03_output_elements.py` | 1. Text, 2. Code and maths |
| badge | `pages/03_output_elements.py` | 3. Badges |
| metric | `pages/03_output_elements.py` | 4. Metrics |
| json | `pages/03_output_elements.py`, `pages/12_embeds_html_json.py` | 5. JSON, 3. st.json |
| success / info / warning / error / exception | `pages/03_output_elements.py` | 6. Status messages |
| toast, balloons | `pages/03_output_elements.py` | 7. Toast and celebrations |
| progress | `pages/04_status_progress.py` | 1. Progress bar |
| spinner | `pages/04_status_progress.py` | 2. Spinner |
| status | `pages/04_status_progress.py` | 3. Status container |
| empty | `pages/04_status_progress.py` | 4. st.empty |
| columns, divider | `pages/05_layouts_containers.py` | 1. Columns |
| tabs | `pages/05_layouts_containers.py` | 2. Tabs |
| expander, popover | `pages/05_layouts_containers.py` | 3. Expander and popover |
| container | `pages/05_layouts_containers.py` | 4. Container |
| sidebar | `pages/05_layouts_containers.py`, `app.py` | 5. Sidebar, 2. Shared sidebar |
| dialog | `pages/05_layouts_containers.py` | 6. Dialog |
| multipage navigation | `app.py` | 1. Declare the pages |
| forms | `pages/06_forms.py` | 1-4 |
| session_state | `pages/07_session_state.py` | 1-4 |
| query_params | `pages/07_session_state.py` | 5. Query params |
| cache_data (ttl) | `pages/08_caching.py` | 1 and 2 |
| cache_resource | `pages/08_caching.py` | 3 |
| fragment, run_every | `pages/08_caching.py` | 4 and 5 |
| chat_input / chat_message / write_stream | `pages/09_chat.py` | 2 and 3 |
| dataframe, table | `pages/10_data_charts.py` | 1. Tables |
| data_editor | `pages/10_data_charts.py` | 2. Editable table |
| bar / line / area / scatter charts | `pages/10_data_charts.py` | 3. Charts |
| map | `pages/10_data_charts.py` | 4. Map |
| CSV upload | `pages/10_data_charts.py` | 5. Upload your own CSV |
| image | `pages/11_media.py` | 1. Image |
| audio | `pages/11_media.py` | 2. Audio |
| video | `pages/11_media.py` | 3. Video |
| camera_input | `pages/11_media.py` | 4. Camera input |
| audio_input | `pages/11_media.py` | 5. Audio input |
| html | `pages/12_embeds_html_json.py` | 1. st.html |
| iframe | `pages/12_embeds_html_json.py` | 2. st.iframe |
| code in several languages | `pages/12_embeds_html_json.py` | 4. st.code |

## 4. "Break it and see" experiments

1. **Remove a key.** In `pages/02_input_widgets.py`, give two widgets the same `key=`. Streamlit raises a duplicate-key error. Now delete `key=` from a widget whose label also matches another widget's: you get a duplicate-ID error. Keys give widgets identity.
2. **Forget the session_state guard.** In `pages/07_session_state.py`, delete the `if "counter" not in st.session_state:` line and set `st.session_state.counter = 0` unconditionally. The counter now resets on every click.
3. **Move code out of a form.** In `pages/06_forms.py`, move the first form's `st.text_input` above the `with st.form(...)` line. It now reruns the page on every keystroke.
4. **Move code into a form.** Put a `st.button` inside a form. Streamlit tells you it must be `st.form_submit_button`.
5. **Change ttl.** In `pages/08_caching.py`, change `ttl=5` to `ttl=1`, then remove the argument. With no ttl the cached time never changes until you clear the cache.
6. **Remove the cache.** Delete `@st.cache_data` above `slow_square`. Every rerun is now slow, even for numbers you used before.
7. **Remove `st.rerun()`** from the `qp_cats` branch on page 07. The URL changes but the text above the buttons lags one click behind.

## 5. Common beginner mistakes and fixes

| Mistake | Symptom | Fix |
|---|---|---|
| Storing a counter in a plain variable | It always resets to its start value | Use `st.session_state` |
| Setting `st.session_state.x = 0` with no guard | The value resets every rerun | `if "x" not in st.session_state:` first |
| Changing a widget's value after it is drawn | `StreamlitAPIException` | Change it in a callback (`on_click`/`on_change`) |
| Using `st.button` inside `if st.button(...)` | The inner button never works, since the outer is False after the click | Store the state in `st.session_state` |
| Slow code at the top of the script | App feels laggy | Wrap it in `st.cache_data` or `st.cache_resource` |
| Two widgets with the same label and no key | `DuplicateWidgetID` error | Give each a unique `key=` |
| Forgetting `st.form_submit_button` | Form raises an error | Every form needs exactly one |
| Expecting a variable to survive a page switch | It is gone | Put it in `st.session_state` |
| Using removed APIs (`st.cache`, `st.experimental_*`) | Deprecation errors | Use `st.cache_data`, `st.query_params`, etc. |

## 6. Next steps

- **Deploy on Community Cloud.** Push the project to GitHub, go to https://share.streamlit.io, pick the repo and set `app.py` as the main file. `requirements.txt` is installed automatically.
- **Secrets.** Put API keys in `.streamlit/secrets.toml` (never commit it) and read them with `st.secrets["name"]`. On Community Cloud paste them into the app's Secrets settings.
- **Connections.** `st.connection("name", type="sql")` gives you a cached, reusable connection to databases and APIs.
- **Testing.** `tests/test_pages.py` uses `streamlit.testing.v1.AppTest`. Extend it: set a widget with `at.slider(key="w_slider").set_value(50).run()` and assert on `at.markdown` or `at.json`.
- **Real chatbot.** Replace the mock generator in `pages/09_chat.py` with a streaming LLM call and keep the rest.
