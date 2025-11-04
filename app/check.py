import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Loads GEMINI_API_KEY from .env

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()

print("\nAvailable Gemini Models for your API key:\n")
for m in models:
    print("-", m.name)
