import os, json, re
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def build_prompt(transcript: str, with_priority: bool = True):
    priority_line = '"priority": "High"|"Medium"|"Low",' if with_priority else ""
    return (
        "You are an expert meeting assistant. Extract clear, actionable tasks from this transcript.\n"
        "Return ONLY valid JSON matching this schema:\n"
        "{\n"
        '  "tasks": [\n'
        "    {\n"
        '      "text": string,\n'
        '      "tags": [string],\n'
        f"      {priority_line}\n"
        "    }\n"
        "  ]\n"
        "}\n\n"
        f'Transcript:\n"""{transcript}"""\n'
    )


def generate_tasks(transcript: str, with_priority: bool = True):
    prompt = build_prompt(transcript, with_priority)

    model = genai.GenerativeModel("gemini-2.5-flash-lite-preview-06-17")

    response = model.generate_content(prompt)

    # Gemini responses are plain text, sometimes wrapped in markdown code fences
    raw = response.text.strip()
    clean = re.sub(r"```(json)?|```", "", raw)

    try:
        data = json.loads(clean)
        return data.get("tasks", [])
    except json.JSONDecodeError:
        print("⚠️ Gemini returned invalid JSON:\n", raw)
        return []
