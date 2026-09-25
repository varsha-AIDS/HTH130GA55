import whisper
import os

model = whisper.load_model("base")


def transcribe_audio(audio_file):

    # If a file path is given
    if isinstance(audio_file, str):

        result = model.transcribe(audio_file)

        return result["text"]

    # If a Streamlit UploadedFile is given
    else:

        import tempfile

        suffix = os.path.splitext(audio_file.name)[1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            temp_file.write(audio_file.getbuffer())
            temp_path = temp_file.name

        try:

            result = model.transcribe(temp_path)

            return result["text"]

        finally:

            if os.path.exists(temp_path):

                os.remove(temp_path)
                

