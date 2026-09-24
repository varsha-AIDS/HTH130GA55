from pyannote.audio import Pipeline

print("Loading speaker diarization model...")

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1"
)

print("Model loaded successfully!")

audio_file = "uploads/01_HR.mp4"

print("Processing:", audio_file)

output = pipeline(audio_file)

print()
print("SPEAKER SEGMENTS")
print("=" * 50)

# Get the actual diarization annotation
diarization = output.speaker_diarization

for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(
        f"{turn.start:.2f}s --> {turn.end:.2f}s : {speaker}"
    )

print()
print("DIARIZATION COMPLETED")