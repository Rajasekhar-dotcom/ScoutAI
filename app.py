import streamlit as st

from dotenv import load_dotenv

from ui.styles import inject_custom_css
from ui.sidebar import render_sidebar
from ui.main_content import render_main_content

from utils.gemini_client import stream_response


# ------------------------------------------------
# Load Environment Variables
# ------------------------------------------------

load_dotenv()


# ------------------------------------------------
# Page Configuration
# ------------------------------------------------

st.set_page_config(

    page_title="Scout AI",

    page_icon="🚀",

    layout="wide",

    initial_sidebar_state="expanded"

)


# ------------------------------------------------
# Inject CSS
# ------------------------------------------------

inject_custom_css()


# ------------------------------------------------
# Session State
# ------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


if "phase" not in st.session_state:

    st.session_state.phase = 0


# ------------------------------------------------
# Render UI
# ------------------------------------------------

render_sidebar()

render_main_content()


# ------------------------------------------------
# User Input
# ------------------------------------------------

user_input = st.chat_input(

    "Ask Scout"

)


# Starter Chips

if getattr(

    st.session_state,

    "_starter",

    None

):

    user_input = st.session_state._starter

    del st.session_state._starter


# ------------------------------------------------
# Process User Message
# ------------------------------------------------

if user_input:

    user_text = user_input.strip()


    # Save User Message

    st.session_state.messages.append(

        {

            "role": "user",

            "content": user_text

        }

    )


    # Display User Message

    with st.chat_message("user"):

        st.markdown(user_text)


    # Assistant Message

    with st.chat_message(

        "assistant",

        avatar="🚀"

    ):


        response_placeholder = st.empty()


        full_response = ""


        try:


            response_stream = stream_response(

                st.session_state.messages

            )


            for chunk in response_stream:


                if (

                    hasattr(chunk, "text")

                    and

                    chunk.text

                ):


                    full_response += chunk.text


                    response_placeholder.markdown(

                        full_response

                    )


            # Save Assistant Response


            st.session_state.messages.append(

                {

                    "role": "assistant",

                    "content": full_response

                }

            )


        except Exception as e:


            error_text = (

                f"⚠️ {str(e)}"

            )


            response_placeholder.markdown(

                error_text

            )


            st.session_state.messages.append(

                {

                    "role": "assistant",

                    "content": error_text

                }

            )


    st.rerun()