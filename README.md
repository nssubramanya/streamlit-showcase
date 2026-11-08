# Streamlit Showcase

A beginner-friendly app that demonstrates every major Streamlit feature. Click through the pages, then read the code behind each one.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Run these from the repository root (the folder containing `app.py`). With uv: `uv run streamlit run app.py`.

## Pages

| Page | Topic |
|---|---|
| 01 Home | The rerun model |
| 02 Input widgets | Buttons, sliders, text, dates, uploads and more |
| 03 Output elements | Text, code, metrics, alerts, toast |
| 04 Status & progress | Progress bars, spinners, status |
| 05 Layouts & containers | Columns, tabs, dialogs, sidebar |
| 06 Forms | Batch inputs with one submit |
| 07 Session state | Remembering values, query params |
| 08 Caching & fragments | Speed and partial reruns |
| 09 Chat | Chat UI with a mock bot (no API key) |
| 10 Data & charts | Tables, editor, charts, map, CSV upload |
| 11 Media | Image, audio, video, camera, microphone |
| 12 Embeds, HTML & code | `st.html`, `st.iframe`, `st.json`, `st.code` |

Look for `# TRY THIS:` comments in the code for things to click or change.

## Checks

```bash
python -m py_compile app.py pages/*.py utils.py   # syntax
pytest tests/ -q                                    # AppTest smoke tests
```

## Learn more

See [docs/EXPLORING_THE_CODE.md](docs/EXPLORING_THE_CODE.md) for a learning path, a feature-to-file table, experiments and common mistakes.

Notes: the video and iframe demos need internet access. Camera and microphone demos need browser permission.
