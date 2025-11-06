import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load token from .env
load_dotenv()
HF_token = os.getenv("HF_token")

# Model details
Model_id = "google/gemma-2-2b-it"
client = InferenceClient(model=Model_id, token=HF_token)

# Initialize chat history
messages = [
    {"role": "system", "content": "You are a friendly, concise assistant. Keep replies clear and short."}
]

def chat_with_bot(user_text: str):
    """
    Sends the user message to the model and returns the assistant's reply.
    """
    global messages
    messages.append({"role": "user", "content": user_text})

    try:
        resp = client.chat_completion(
            messages=messages,
            max_tokens=300,
            temperature=0.5,
            top_p=0.9,
            stop=["\nUser:", "\nSystem:"]
        )
        bot_text = resp.choices[0].message["content"]
        messages.append({"role": "assistant", "content": bot_text})
        return bot_text

    except Exception as e:
        messages.pop()  # Remove last user input if error
        return f"Error: {e}"
