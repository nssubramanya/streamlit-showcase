"""Chat: build a chatbot UI with a MOCK bot (no API key needed).

Demonstrates: st.chat_input, st.chat_message, st.write_stream, st.session_state
for keeping the conversation history.

To use a real AI later, replace `mock_reply_words` with a call to an LLM that
streams its answer - the Streamlit parts stay exactly the same.
"""

import time

import streamlit as st

st.title("💬 Chat")
st.caption("A fake bot that echoes your message with a typing effect.")


# ---------- 1. The mock bot ----------
def mock_reply_words(user_text: str):
    """A generator: yields one word at a time, like a streaming LLM."""
    reply = f"You said: '{user_text}'. I'm a mock bot, so I can only repeat that. Nice to meet you!"
    for word in reply.split():
        time.sleep(0.05)  # small pause = visible typing effect
        yield word + " "


# ---------- 2. Conversation history ----------
# The script reruns on every message, so history must live in session_state.
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hi! Type a message below."}
    ]

# Redraw all earlier messages on every rerun.
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):  # role: "user" or "assistant"
        st.write(message["content"])

# ---------- 3. New message ----------
# TRY THIS: type a message and press Enter. chat_input sticks to the page bottom.
prompt = st.chat_input("Say something...", key="chat_box")
if prompt:
    # Show and remember the user's message.
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # write_stream displays a generator live and RETURNS the full text.
    with st.chat_message("assistant"):
        full_reply = st.write_stream(mock_reply_words(prompt))
    st.session_state.chat_history.append({"role": "assistant", "content": full_reply})

# ---------- 4. Reset ----------
# TRY THIS: click to start a new conversation.
if st.sidebar.button("Clear chat", key="chat_clear"):
    del st.session_state.chat_history
    st.rerun()
st.caption("Idea: history in session_state + a loop to redraw it = a chat app.")
