import torch
import soundfile as sf
from pyannote.audio import Pipeline

print("Loading speaker diarization model...")

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1"
)

print("Model loaded successfully!")


def diarize_audio(audio_file):

    print("Processing:", audio_file)

    # Load audio using SoundFile instead of TorchCodec
    waveform, sample_rate = sf.read(audio_file, dtype="float32")

    # Convert NumPy array → PyTorch tensor
    waveform = torch.from_numpy(waveform)

    # If stereo, convert to [channel, time]
    if waveform.ndim == 1:
        waveform = waveform.unsqueeze(0)
    else:
        waveform = waveform.T

    audio = {
        "waveform": waveform,
        "sample_rate": sample_rate
    }

    output = pipeline(audio)

    diarization = output.speaker_diarization

    speaker_segments = []

    for turn, _, speaker in diarization.itertracks(yield_label=True):

        speaker_segments.append({
            "start": turn.start,
            "end": turn.end,
            "speaker": speaker
        })

    return speaker_segments