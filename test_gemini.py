import os
from google import genai


# ============================================================
# CHECK API KEY
# ============================================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found!")
    exit()


# ============================================================
# CREATE GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=api_key
)


# ============================================================
# TEST GEMINI
# ============================================================

print("=" * 60)
print("TESTING GEMINI CONNECTION")
print("=" * 60)

try:

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input="Say hello in one short sentence."
    )

    print()
    print("Gemini connection successful!")
    print()
    print(interaction.output_text)

except Exception as error:

    print()
    print("Gemini connection failed!")
    print(error)
    
