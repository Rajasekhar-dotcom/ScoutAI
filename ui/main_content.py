# ui/main_content.py
import streamlit as st

def render_main_content():
    st.markdown('<div class="chat-header">💬 Conversation</div>', unsafe_allow_html=True)

    if not st.session_state.messages:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-orb">🚀</div>
            <h3>Ready to build your startup?</h3>
            <p>Scout AI is ready. Share your domain, budget, and target customers to get started.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(
            "<p style='text-align:center;color:#4A5278;font-size:0.8rem;margin-top:1.5rem;'>Try one of these to start:</p>",
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns(3, gap="medium")

        with c1:
            if st.button("🤖 AI / SaaS", use_container_width=True):
                st.session_state._starter = "I want to build something in AI / SaaS"
                st.rerun()

        with c2:
            if st.button("🌱 Climate Tech", use_container_width=True):
                st.session_state._starter = "I'm interested in climate tech startups"
                st.rerun()

        with c3:
            if st.button("🏥 HealthTech", use_container_width=True):
                st.session_state._starter = "I want to explore HealthTech opportunities"
                st.rerun()
    else:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"], avatar="🚀" if msg["role"] == "assistant" else None):
                st.markdown(msg["content"])