# app.py
import streamlit as st
from dotenv import load_dotenv
from ui.styles import inject_custom_css
from ui.sidebar import render_sidebar
from ui.main_content import render_main_content
from utils.gemini_client import get_or_create_chat

load_dotenv()

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Scout AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject Global Styles
inject_custom_css()

# ── Session State Initialization ───────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_session" not in st.session_state:
    st.session_state.chat_session = None

if "phase" not in st.session_state:
    st.session_state.phase = 0

# ── Render UI Panels ───────────────────────────────────────────────────────────
render_sidebar()
render_main_content()

# ── Handle Input and Starter Chips ─────────────────────────────────────────────
user_input = st.chat_input("Ask Scout")

if getattr(st.session_state, "_starter", None):
    user_input = st.session_state._starter
    del st.session_state._starter

# ── Process Stream Response Lifecycle ──────────────────────────────────────────
if user_input:
    user_text = user_input.strip()
    st.session_state.messages.append({"role": "user", "content": user_text})
    
    with st.chat_message("user"):
        st.markdown(user_text)

    chat = get_or_create_chat()
    if chat is None:
        error_msg = "⚠️ No API key found. Please set `api_key` in your `.env` file and restart the app."
        st.session_state.messages.append({"role": "ai", "content": error_msg})
        with st.chat_message("ai", avatar="🚀"):
            st.markdown(error_msg)
    else:
        with st.chat_message("ai", avatar="🚀"):
            response_placeholder = st.empty()
            with st.spinner("Scouting data..."):
                try:
                    response_stream = chat.send_message_stream(user_text)
                    full_response = ""
                    for chunk in response_stream:
                        if chunk.text:
                            full_response += chunk.text
                            response_placeholder.markdown(full_response)
                    st.session_state.messages.append({"role": "ai", "content": full_response})
                except Exception as e:
                    error_text = f"⚠️ Something went wrong: {str(e)}"
                    response_placeholder.markdown(error_text)
                    st.session_state.messages.append({"role": "ai", "content": error_text})

    st.rerun()