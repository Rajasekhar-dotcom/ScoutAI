# utils/gemini.py
import os
import streamlit as st
from google import genai
from google.genai import types
from prompts.system_prompt import SYSTEM_PROMPT

PHASES = [
    ("Intro",          "🎯"),
    ("Gather Info",    "📋"),
    ("Generate Ideas", "💡"),
    ("Deep Dive",      "🔬"),
    ("Complete",       "✅"),
]

@st.cache_resource
def get_client():
    api_key = os.getenv("api_key") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

def get_or_create_chat():
    if st.session_state.chat_session is None:
        client = get_client()
        if client is None:
            return None
        config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
        st.session_state.chat_session = client.chats.create(
            model="gemini-3.1-flash-lite", config=config
        )
    return st.session_state.chat_session

def detect_phase(messages):
    if len(messages) == 0:
        return 0
    text = " ".join(m["content"].lower() for m in messages if m["role"] == "ai")
    if "elevator pitch" in text:
        return 4
    if "problem statement" in text or "market size" in text:
        return 3
    if "choose" in text or "which idea" in text or "pick" in text:
        return 2
    if "domain" in text or "budget" in text or "target" in text:
        return 1
    return 1