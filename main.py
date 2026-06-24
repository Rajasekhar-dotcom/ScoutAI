import os
from dotenv import load_dotenv
from prompts.system_prompt import SYSTEM_PROMPT
from google import genai
from google.genai import types
from utils.cli_ui import welcome

load_dotenv()

API_KEY = os.getenv('api_key')

client = genai.Client(api_key = API_KEY)
config = types.GenerateContentConfig(
    system_instruction = SYSTEM_PROMPT
)

chat = client.chats.create(model = "gemini-3.1-flash-lite",
                           config = config)

print(welcome())

while True:
    try:
        user_prompt = input("You: ")
        if user_prompt.strip().lower() in ['exit', 'quit']:
            print("Sad to see you leave so soon...")
            break
        if not user_prompt.strip():
            continue
        response = chat.send_message_stream(user_prompt)

        for chunk in response:
            if chunk.text is not None:
                print(chunk.text, end = "", flush = True)
        print("\n")
    
    except KeyboardInterrupt:
        print("Sad to see you leave so soon...")
        break
    except ConnectionError:
        print("Please check you internet connection and try again")
        break
    except TimeoutError:
        print("Gemini took too long to respond. Try again after sometime")
        break
    except Exception as e:
        print(f"An unknown error has occurred: {e}")
        break