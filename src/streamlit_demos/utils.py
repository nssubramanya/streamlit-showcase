"""Tiny shared helpers used by more than one page.

Everything else lives inside the page that uses it, so each page stays readable
on its own.  Covers: st.cache_data (for the sample-data loader).
"""

import io
import wave
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

# Folder that contains this file, so paths work no matter where you run from.
APP_DIR = Path(__file__).parent


@st.cache_data
def load_sales() -> pd.DataFrame:
    """Read data/sales.csv once and remember the result (cached)."""
    return pd.read_csv(APP_DIR / "data" / "sales.csv", parse_dates=["date"])


def make_wav_bytes(freq: float = 440.0, seconds: float = 1.5) -> bytes:
    """Generate a sine-wave WAV file in memory (no audio file needed)."""
    rate = 22050
    t = np.linspace(0, seconds, int(rate * seconds), endpoint=False)
    samples = (np.sin(2 * np.pi * freq * t) * 0.4 * 32767).astype(np.int16)
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav:
        wav.setnchannels(1)  # mono
        wav.setsampwidth(2)  # 16-bit
        wav.setframerate(rate)
        wav.writeframes(samples.tobytes())
    return buffer.getvalue()
