import os
import json
from google import genai

INPUT_FILE = "final_transcript.txt"
OUTPUT_FILE = "action_items.txt"

# --------------------------------------------------
# 1. Get API key
# --------------------------------------------------

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found!")
    exit()

# --------------------------------------------------
# 2. Connect to Gemini
# --------------------------------------------------

client = genai.Client(
    api_key=api_key
)

# --------------------------------------------------
# 3. Read meeting transcript
# --------------------------------------------------

print("=" * 60)
print("READING MEETING TRANSCRIPT")
print("=" * 60)

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    transcript = file.read()

print("Transcript loaded successfully!")
print()

# --------------------------------------------------
# 4. Create prompt
# --------------------------------------------------

prompt = f"""
You are an AI meeting accountability assistant.

Analyze the following meeting transcript.

Extract all action items.

For each action item identify:

1. task
2. owner
3. deadline
4. status
5. evidence

Also extract:

6. decisions
7. unresolved_items

Return ONLY valid JSON.

Use exactly this format:

{{
    "action_items": [
        {{
            "task": "string",
            "owner": "string or null",
            "deadline": "string or null",
            "status": "new",
            "evidence": "string"
        }}
    ],
    "decisions": [],
    "unresolved_items": []
}}

Meeting transcript:

{transcript}
"""

# --------------------------------------------------
# 5. Send transcript to Gemini
# --------------------------------------------------

print("=" * 60)
print("ANALYZING MEETING WITH GEMINI")
print("=" * 60)

try:

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    result_text = interaction.output_text.strip()

    print("Gemini analysis completed!")
    print()

except Exception as error:

    print("Gemini analysis failed!")
    print(error)
    exit()

# --------------------------------------------------
# 6. Convert Gemini response to JSON
# --------------------------------------------------

try:

    result = json.loads(result_text)

except json.JSONDecodeError:

    print("Gemini did not return valid JSON.")
    print()
    print(result_text)
    exit()

# --------------------------------------------------
# 7. Save action items
# --------------------------------------------------

with open(OUTPUT_FILE, "w", encoding="utf-8") as output:

    output.write("ACTION ITEMS\n")
    output.write("============\n\n")

    for item in result.get("action_items", []):

        output.write(
            f"Owner: {item.get('owner')}\n"
        )

        output.write(
            f"Task: {item.get('task')}\n"
        )

        output.write(
            f"Deadline: {item.get('deadline')}\n"
        )

        output.write(
            f"Status: {item.get('status')}\n"
        )

        output.write(
            f"Evidence: {item.get('evidence')}\n"
        )

        output.write("\n")

    output.write("DECISIONS\n")
    output.write("=========\n\n")

    for decision in result.get("decisions", []):

        output.write(
            f"- {decision}\n"
        )

    output.write("\n")

    output.write("UNRESOLVED ITEMS\n")
    output.write("================\n\n")

    for item in result.get("unresolved_items", []):

        output.write(
            f"- {item}\n"
        )

# --------------------------------------------------
# 8. Display result
# --------------------------------------------------

print("=" * 60)
print("ACTION ITEMS")
print("=" * 60)

for item in result.get("action_items", []):

    print()
    print("Owner:", item.get("owner"))
    print("Task:", item.get("task"))
    print("Deadline:", item.get("deadline"))
    print("Status:", item.get("status"))
    print("Evidence:", item.get("evidence"))

print()
print("=" * 60)
print("GENAI ACTION ITEM EXTRACTION COMPLETED!")
print("=" * 60)

print()
print("Created:")
print(OUTPUT_FILE)
