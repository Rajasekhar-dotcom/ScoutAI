import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght=400;500;600;700&family=Inter:wght=400;500&display=swap');

    /* ── Base ── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0A0E1A;
        color: #E8E6F0;
    }

    .stApp { background-color: #0A0E1A; }

    /* ── Hide Streamlit chrome ── */
    #MainMenu, footer { visibility: hidden; }
    [data-testid="stHeader"] {
        background-color: transparent !important;
        backdrop-filter: none !important;
    }
    [data-testid="stActionButton"] { display: none !important; }
    .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: #0F1525;
        border-right: 1px solid #1E2A45;
    }

    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .stMarkdown li {
        color: #A0A8C0;
        font-size: 0.85rem;
    }

    /* ── Logo / Title ── */
    .brand-header {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 1.6rem;
        color: #E8E6F0;
        letter-spacing: -0.5px;
        margin-bottom: 0.15rem;
    }

    .brand-sub {
        font-size: 0.78rem;
        color: #6C63FF;
        font-weight: 500;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }

    /* ── Step tracker ── */
    .step-item {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 7px 10px;
        border-radius: 8px;
        margin-bottom: 4px;
        font-size: 0.82rem;
        color: #6B7BA4;
        transition: background 0.2s;
    }
    .step-item.active {
        background: #1A2245;
        color: #6C63FF;
        font-weight: 600;
    }
    .step-item.done { color: #4ADE80; }
    .step-dot {
        width: 8px; height: 8px;
        border-radius: 50%;
        background: currentColor;
        flex-shrink: 0;
    }

    /* ── Divider ── */
    .sidebar-divider {
        border: none;
        border-top: 1px solid #1E2A45;
        margin: 1.2rem 0;
    }

    /* ── Chat container ── */
    .chat-header {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.15rem;
        font-weight: 600;
        color: #E8E6F0;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #1E2A45;
        margin-bottom: 1rem;
    }

    /* ── Message bubbles ── */
    .msg-user { display: flex; justify-content: flex-end; margin-bottom: 1rem; }
    .msg-user .bubble {
        background: #6C63FF;
        color: #fff;
        border-radius: 18px 18px 4px 18px;
        padding: 12px 18px;
        max-width: 72%;
        font-size: 0.92rem;
        line-height: 1.55;
        box-shadow: 0 2px 12px rgba(108,99,255,0.25);
    }

    .msg-ai { display: flex; justify-content: flex-start; margin-bottom: 1rem; gap: 10px; }
    .ai-avatar {
        width: 36px; height: 36px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6C63FF, #A855F7);
        display: flex; align-items: center; justify-content: center;
        font-size: 1rem;
        flex-shrink: 0;
        box-shadow: 0 0 16px rgba(108,99,255,0.35);
    }
    .msg-ai .bubble {
        background: #131929;
        border: 1px solid #1E2A45;
        color: #D0CEE8;
        border-radius: 4px 18px 18px 18px;
        padding: 14px 18px;
        max-width: 78%;
        font-size: 0.92rem;
        line-height: 1.65;
    }
    .msg-ai .bubble strong { color: #E8E6F0; }
    .msg-ai .bubble h3 {
        font-family: 'Space Grotesk', sans-serif;
        color: #6C63FF;
        font-size: 0.95rem;
        margin: 0.8rem 0 0.3rem;
    }
    .msg-ai .bubble ul { padding-left: 1.2rem; margin: 0.4rem 0; }
    .msg-ai .bubble li { margin-bottom: 0.3rem; }
    .msg-ai .bubble hr { border-color: #1E2A45; margin: 0.8rem 0; }

    /* ── Input area ── */
    .input-wrapper {
        background: #0F1525;
        border: 1px solid #1E2A45;
        border-radius: 14px;
        padding: 4px 8px 4px 16px;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 1rem;
        transition: border-color 0.2s;
    }
    .input-wrapper:focus-within {
        border-color: #6C63FF;
        box-shadow: 0 0 0 3px rgba(108,99,255,0.12);
    }

    .stTextInput > div > div > input {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #E8E6F0 !important;
        font-size: 0.92rem;
        padding: 10px 0 !important;
    }
    .stTextInput > div > div > input::placeholder { color: #4A5278; }
    .stTextInput > div { border: none !important; background: transparent !important; }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #6C63FF, #A855F7) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.45rem 1.2rem !important;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.3px;
        transition: opacity 0.15s, transform 0.1s !important;
        cursor: pointer;
    }
    .stButton > button:hover {
        opacity: 0.88 !important;
        transform: translateY(-1px) !important;
    }
    .stButton > button:active { transform: translateY(0px) !important; }

    [data-testid="stMain"] div[data-testid="stColumn"] .stButton { width: 100%; }
    [data-testid="stMain"] div[data-testid="stColumn"] .stButton > button { width: 100% !important; height: 52px; }

    .reset-btn > button {
        background: transparent !important;
        border: 1px solid #2A3350 !important;
        color: #6B7BA4 !important;
        font-size: 0.78rem !important;
        padding: 0.35rem 0.9rem !important;
        border-radius: 8px !important;
    }
    .reset-btn > button:hover {
        border-color: #FF6B6B !important;
        color: #FF6B6B !important;
        opacity: 1 !important;
        transform: none !important;
    }

    /* ── Pulse orb ── */
    @keyframes pulse-ring {
        0%   { transform: scale(0.85); opacity: 0.7; }
        50%  { transform: scale(1.05); opacity: 1;   }
        100% { transform: scale(0.85); opacity: 0.7; }
    }
    .thinking-orb {
        width: 36px; height: 36px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6C63FF, #A855F7);
        animation: pulse-ring 1.4s ease-in-out infinite;
        display: flex; align-items: center; justify-content: center;
        font-size: 1rem;
        box-shadow: 0 0 20px rgba(108,99,255,0.5);
    }

    /* ── Empty state ── */
    .empty-state { text-align: center; padding: 3rem 1rem; }
    .empty-orb {
        width: 72px; height: 72px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6C63FF22, #A855F722);
        border: 1px solid #6C63FF44;
        margin: 0 auto 1.2rem;
        display: flex; align-items: center; justify-content: center;
        font-size: 2rem;
    }
    .empty-state h3 {
        font-family: 'Space Grotesk', sans-serif;
        color: #E8E6F0;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
    }
    .empty-state p { color: #5A6480; font-size: 0.88rem; max-width: 320px; margin: 0 auto; line-height: 1.6; }

    /* Scrollable chat area */
    .chat-scroll {
        max-height: 62vh;
        overflow-y: auto;
        padding-right: 4px;
        scrollbar-width: thin;
        scrollbar-color: #1E2A45 transparent;
    }
    .chat-scroll::-webkit-scrollbar { width: 5px; }
    .chat-scroll::-webkit-scrollbar-thumb { background: #1E2A45; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)