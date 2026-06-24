import streamlit as st
from utils.gemini_client import detect_phase, PHASES, get_client

def render_sidebar():
    with st.sidebar:
        st.markdown('<div class="brand-header">Scout AI</div>', unsafe_allow_html=True)
        st.markdown('<div class="brand-sub">Startup Intelligence</div>', unsafe_allow_html=True)

        # Progress steps
        phase = detect_phase(st.session_state.messages)
        for i, (label, icon) in enumerate(PHASES):
            cls = "done" if i < phase else ("active" if i == phase else "")
            check = "✓" if i < phase else icon
            st.markdown(
                f'<div class="step-item {cls}"><span class="step-dot"></span>{check} {label}</div>',
                unsafe_allow_html=True
            )

        st.markdown('<hr class="sidebar-divider"/>', unsafe_allow_html=True)

        st.markdown("**About this tool**")
        st.markdown("""
    - Guided by real YC frameworks
    - Covers TAM/SAM/SOM, MVP, GTM
    - Structured for first-time founders
    - Iterative, no assumptions made
    """)

        st.markdown('<hr class="sidebar-divider"/>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
            if st.button("🔄 New Session"):
                st.session_state.messages = []
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # API key status
        client = get_client()
        if client:
            st.markdown('<p style="color:#4ADE80;font-size:0.75rem;margin-top:1rem;">● API Connected</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="color:#FF6B6B;font-size:0.75rem;margin-top:1rem;">● No API Key Found</p>', unsafe_allow_html=True)
            st.markdown('<p style="color:#6B7BA4;font-size:0.75rem;">Set <code>api_key</code> in your .env file</p>', unsafe_allow_html=True)