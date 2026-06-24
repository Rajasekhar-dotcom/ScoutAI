import os

import streamlit as st

from google import genai

from google.genai import types

from prompts.system_prompt import SYSTEM_PROMPT


PHASES = [

    ("Intro", "🎯"),

    ("Gather Info", "📋"),

    ("Generate Ideas", "💡"),

    ("Deep Dive", "🔬"),

    ("Complete", "✅"),

]


@st.cache_resource
def get_client():
    api_key = None

    try:
        api_key = st.secrets["api_key"]
    except:
        pass

    if api_key is None:
        api_key = (
            os.getenv("api_key")
            or
            os.getenv("GOOGLE_API_KEY")
        )

    if not api_key:
        return None

    return genai.Client(
        api_key=api_key
    )


    if not api_key:

        return None


    return genai.Client(api_key=api_key)




def stream_response(messages):

    client = get_client()


    if client is None:

        raise ValueError(

            "No API Key Found"

        )


    contents = []


    for msg in messages:


        role = (

            "user"

            if msg["role"] == "user"

            else "model"

        )


        contents.append(

            {

                "role": role,

                "parts": [

                    {

                        "text": msg["content"]

                    }

                ]

            }

        )



    config = types.GenerateContentConfig(

        system_instruction=SYSTEM_PROMPT

    )



    response = client.models.generate_content_stream(

        model="gemini-3.1-flash-lite",

        contents=contents,

        config=config

    )


    return response




def detect_phase(messages):

    if len(messages) == 0:

        return 0


    text = " ".join(

        m["content"].lower()

        for m in messages

        if m["role"] == "assistant"

    )


    if "elevator pitch" in text:

        return 4


    if (

        "problem statement" in text

        or

        "market size" in text

    ):

        return 3


    if (

        "choose" in text

        or

        "which idea" in text

        or

        "pick" in text

    ):

        return 2


    if (

        "domain" in text

        or

        "budget" in text

        or

        "target" in text

    ):

        return 1


    return 1