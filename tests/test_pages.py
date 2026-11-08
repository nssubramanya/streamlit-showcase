"""Smoke tests: open every page through the real app (app.py) with Streamlit's
AppTest and check that it runs without raising an exception.

We go through app.py (instead of loading a page file alone) because pages use
st.page_link, which only works inside st.navigation.

Run with:  pytest tests/ -q   (from the folder that contains app.py)
"""

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

APP_DIR = Path(__file__).parent.parent
PAGES = sorted(p.relative_to(APP_DIR).as_posix() for p in (APP_DIR / "pages").glob("*.py"))


def test_there_are_twelve_pages():
    assert len(PAGES) == 12


def test_entrypoint_runs_without_exception():
    at = AppTest.from_file(str(APP_DIR / "app.py"), default_timeout=30).run()
    assert not at.exception, [e.value for e in at.exception]


@pytest.mark.parametrize("page", PAGES)
def test_page_runs_without_exception(page):
    at = AppTest.from_file(str(APP_DIR / "app.py"), default_timeout=30).run()
    at.switch_page(page).run()
    assert not at.exception, [e.value for e in at.exception]
