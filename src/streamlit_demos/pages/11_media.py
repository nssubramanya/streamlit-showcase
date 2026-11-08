"""Media: images, audio, video and live capture from camera/microphone.

Demonstrates: st.image, st.audio, st.video, st.camera_input, st.audio_input.

All sample media is generated in code (PIL / numpy), so nothing is downloaded.
"""

import numpy as np
import streamlit as st
from PIL import Image

from utils import make_wav_bytes

st.title("🖼️ Media")

# ---------- 1. Image ----------
st.header("1. Image")


def make_gradient_image(red_level: int) -> Image.Image:
    """Build a 256x256 colour gradient with numpy, then turn it into a PIL image."""
    x = np.tile(np.linspace(0, 255, 256), (256, 1))  # left -> right
    y = x.T  # top -> bottom
    pixels = np.stack([np.full_like(x, red_level), x, y], axis=-1).astype(np.uint8)
    return Image.fromarray(pixels)


# TRY THIS: move the slider and the generated picture changes colour.
red = st.slider("Amount of red", 0, 255, 120, key="media_red")
st.image(make_gradient_image(red), caption="Generated with numpy + PIL", width=256)
st.caption("Idea: st.image accepts PIL images, numpy arrays, file paths and URLs.")

# ---------- 2. Audio ----------
st.header("2. Audio")

# TRY THIS: change the pitch, then press play. The WAV file is made in memory.
pitch = st.select_slider("Pitch (Hz)", options=[220, 330, 440, 660, 880], value=440, key="media_pitch")
st.audio(make_wav_bytes(freq=pitch), format="audio/wav")
st.caption("Idea: st.audio takes raw bytes, a file path or a URL.")

# ---------- 3. Video ----------
st.header("3. Video")

# TRY THIS: press play. This uses a public URL, so it needs internet access.
# For a local file use st.video("my_video.mp4") with the path to your file.
st.video("https://static.streamlit.io/examples/star.mp4")
st.caption("Idea: st.video accepts a URL, a local path or bytes. Local files work offline.")

# ---------- 4. Camera ----------
st.header("4. Camera input")

# TRY THIS: allow camera access in your browser and take a photo.
photo = st.camera_input("Take a picture", key="media_camera")
if photo is not None:
    picture = Image.open(photo)
    st.write({"width": picture.width, "height": picture.height})
    st.image(picture.convert("L"), caption="Your photo in greyscale", width=256)
else:
    st.info("No photo yet - the widget returns None until you take one.")
st.caption("Idea: camera_input returns an image file you can open with PIL.")

# ---------- 5. Audio input ----------
st.header("5. Audio input (microphone)")

# TRY THIS: click the microphone, record a few seconds, then stop.
recording = st.audio_input("Record a voice message", key="media_mic")
if recording is not None:
    st.audio(recording)  # play it back
    st.write({"size_bytes": recording.size, "type": recording.type})
else:
    st.info("No recording yet - the widget returns None until you record.")
st.caption("Idea: audio_input returns a WAV file object you can play or process.")
