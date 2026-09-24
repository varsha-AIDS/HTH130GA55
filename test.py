import os
from faster_whisper import WhisperModel


# Folder containing your 26 recordings
UPLOAD_FOLDER = "uploads"

# Folder for transcripts
OUTPUT_FOLDER = "transcripts"

# Create transcripts folder automatically
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# Load Whisper
print("Loading Whisper model...")
print("Please wait...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Whisper model loaded!")
print()


# Get all MP4 files
files = [
    file
    for file in os.listdir(UPLOAD_FOLDER)
    if file.lower().endswith(".mp4")
]

# Sort 01, 02, 03 ... 26
files.sort()


print("Number of files found:", len(files))
print()


# Transcribe each file
for file in files:

    print("----------------------------------------")
    print("Processing:", file)
    print("----------------------------------------")

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file
    )

    # Convert speech to text
    segments, info = model.transcribe(
        file_path
    )

    transcript = ""

    for segment in segments:
        transcript += segment.text.strip() + " "

    transcript = transcript.strip()


    # Create output file
    file_name = os.path.splitext(file)[0]

    output_path = os.path.join(
        OUTPUT_FOLDER,
        file_name + ".txt"
    )


    # Save transcript
    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(transcript)


    print("Saved:", output_path)
    print()


print("========================================")
print("TRANSCRIPTION COMPLETED")
print("========================================")
