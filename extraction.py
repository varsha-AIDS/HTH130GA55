
import json
import os
from pathlib import Path

from google import genai
from google.genai import types
from dotenv import load_dotenv


# Load API key from .env
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY not found.")
    exit()


# Create Gemini client
client = genai.Client(
    api_key=api_key
)


def extract_meeting_info(transcript):

    prompt = f"""
You are an AI meeting accountability assistant.

Analyze the meeting transcript below.

Extract ONLY information explicitly mentioned in the transcript.
Do NOT guess or invent any information.

Rules:

1. Do not invent tasks.
2. Do not invent owners.
3. Do not invent deadlines.
4. If the owner is not mentioned, use null.
5. If the deadline is not mentioned, use null.
6. Evidence must be an exact sentence from the transcript.
7. If something is uncertain, put it under unresolved_items.

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

        return {
            "error": str(e)
        }


# Main program
if __name__ == "__main__":

    print("=" * 60)
    print("AI MEETING ACCOUNTABILITY")
    print("GEMINI EXTRACTION")
    print("=" * 60)

    # Read transcript
    with open(
        "final_transcript.txt",
        "r",
        encoding="utf-8"
    ) as file:

        transcript = file.read()

    print()
    print("Transcript loaded successfully!")

    # Extract information
    print()
    print("Analyzing meeting with Gemini...")

    result = extract_meeting_info(transcript)

    # Display result
    print()
    print("=" * 60)
    print("MEETING ANALYSIS")
    print("=" * 60)

    print(
        json.dumps(
            result,
            indent=4,
            ensure_ascii=False
        )
    )

    # Save result
    with open(
        "meeting_analysis.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False
        )

    print()
    print("=" * 60)
    print("EXTRACTION COMPLETED")
    print("=" * 60)

    print()
    print("Created file:")
    print("meeting_analysis.json")
    