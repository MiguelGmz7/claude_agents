import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_openai_client():
    """Initialize and return an OpenAI client instance."""
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    client = OpenAI(api_key=api_key)
    return client

# Initialize the client
openai_client = get_openai_client()
print("OpenAI client configured.")
