import json
import os
from pathlib import Path

from google import genai
from google.genai import types
from dotenv import load_dotenv


# Load API key from DATA/.env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_meeting_info(transcript):

    prompt = f"""
You are an AI meeting accountability assistant.

Analyze the meeting transcript below.

Extract ONLY information explicitly mentioned in the transcript.
Do NOT guess or invent any information.

If the owner is not mentioned, use null.
If the deadline is not mentioned, use null.

Return ONLY valid JSON in this format:

{{
    "action_items": [
        {{
            "task": "string",
            "owner": "string or null",
            "deadline": "string or null",
            "status": "new, carried_over, overdue, completed, or unresolved",
            "evidence": "exact sentence from transcript"
        }}
    ],
    "decisions": [
        "decision text"
    ],
    "unresolved_items": [
        {{
            "issue": "string",
            "evidence": "exact sentence from transcript"
        }}
    ]
}}

Meeting transcript:
{transcript}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )

        return json.loads(response.text)

    except Exception as e:
        return {"error": str(e)}