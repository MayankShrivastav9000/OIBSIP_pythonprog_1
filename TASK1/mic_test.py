import sounddevice as sd
import numpy as np

print("Script started")

duration = 3
sample_rate = 44100

print("About to record")
audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype='float32'
)
sd.wait()

print("Recording finished")
print("Audio shape:", audio.shape)
print("Max amplitude:", np.max(np.abs(audio)))
