import os
from faster_whisper import WhisperModel
from pyannote.audio import Pipeline


# ============================================================
# SETTINGS
# ============================================================

UPLOAD_FOLDER = "uploads"
OUTPUT_FILE = "final_transcript.txt"

WHISPER_MODEL = "base"


# ============================================================
# LOAD WHISPER MODEL
# ============================================================

print("=" * 60)
print("LOADING WHISPER MODEL")
print("=" * 60)

whisper_model = WhisperModel(
    WHISPER_MODEL,
    device="cpu",
    compute_type="int8"
)

print("Whisper model loaded successfully!")
print()


# ============================================================
# LOAD SPEAKER DIARIZATION MODEL
# ============================================================

print("=" * 60)
print("LOADING SPEAKER DIARIZATION MODEL")
print("=" * 60)

diarization_pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1"
)

print("Speaker diarization model loaded successfully!")
print()


# ============================================================
# FUNCTION TO FIND SPEAKER
# ============================================================

def get_speaker(start_time, end_time, diarization):

    best_speaker = "UNKNOWN"
    best_overlap = 0

    for turn, _, speaker in diarization.itertracks(
        yield_label=True
    ):

        overlap_start = max(
            start_time,
            turn.start
        )

        overlap_end = min(
            end_time,
            turn.end
        )

        overlap = max(
            0,
            overlap_end - overlap_start
        )

        if overlap > best_overlap:
            best_overlap = overlap
            best_speaker = speaker

    return best_speaker


# ============================================================
# GET SPEAKER NAME FROM FILE NAME
# ============================================================

def get_speaker_name(filename):

    # Example:
    # 01_HR.mp4       -> HR
    # 02_POOJA.mp4    -> POOJA
    # 10_PRATHIKSHA.mp4 -> PRATHIKSHA

    name_without_extension = os.path.splitext(filename)[0]

    parts = name_without_extension.split("_")

    if len(parts) >= 2:
        return parts[1].upper()

    return "UNKNOWN"


# ============================================================
# FIND ALL MP4 FILES IN uploads
# ============================================================

files = [
    file
    for file in os.listdir(UPLOAD_FOLDER)
    if file.lower().endswith(".mp4")
]

files.sort()


print("=" * 60)
print(f"FOUND {len(files)} VIDEO FILES")
print("=" * 60)

for file in files:
    print(file)

print()


# ============================================================
# CREATE FINAL TRANSCRIPT FILE
# ============================================================

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as output:

    # Clean heading
    output.write("MEETING TRANSCRIPT\n")
    output.write("==================\n\n")


    # ========================================================
    # PROCESS ALL FILES
    # ========================================================

    for index, filename in enumerate(
        files,
        start=1
    ):

        file_path = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        print()
        print("=" * 60)
        print(
            f"PROCESSING FILE {index}/{len(files)}"
        )
        print(filename)
        print("=" * 60)


        # ====================================================
        # GET SPEAKER NAME
        # ====================================================

        speaker_name = get_speaker_name(filename)

        print(
            f"Speaker identified as: {speaker_name}"
        )


        # ====================================================
        # TRANSCRIPTION
        # ====================================================

        print("Transcribing audio...")

        segments, info = whisper_model.transcribe(
            file_path,
            beam_size=5,
            vad_filter=True
        )

        segments = list(segments)

        print(
            f"Transcription completed. "
            f"{len(segments)} segments found."
        )


        # ====================================================
        # SPEAKER DIARIZATION
        # ====================================================

        print("Detecting speakers...")

        diarization_output = diarization_pipeline(
            file_path
        )

        diarization = (
            diarization_output.speaker_diarization
        )

        print(
            "Speaker detection completed."
        )


        # ====================================================
        # WRITE CLEAN CONVERSATION
        # ====================================================

        for segment in segments:

            start = segment.start
            end = segment.end

            text = segment.text.strip()

            if not text:
                continue


            # Find detected speaker
            detected_speaker = get_speaker(
                start,
                end,
                diarization
            )


            # Use the name from the file
            speaker = speaker_name


            # Write clean conversation
            output.write(
                f"{speaker}: {text}\n\n"
            )


    # ========================================================
    # END OF TRANSCRIPT
    # ========================================================

    output.write(
        "==================\n"
    )

    output.write(
        "END OF MEETING TRANSCRIPT\n"
    )


# ============================================================
# COMPLETED
# ============================================================

print()
print("=" * 60)
print("ALL FILES PROCESSED SUCCESSFULLY!")
print("=" * 60)

print()
print("Final transcript created:")
print(OUTPUT_FILE)
print()
