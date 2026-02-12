import speech_recognition as sr
import sounddevice as sd
import numpy as np

recognizer = sr.Recognizer()

duration = 5
sample_rate = 44100

print("Speak clearly now...")

# Record audio
audio_float = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="float32"
)
sd.wait()

# Convert float32 (-1.0 to 1.0) → int16
audio_float = np.squeeze(audio_float)

# Normalize (important)
max_val = np.max(np.abs(audio_float))
if max_val > 0:
    audio_float = audio_float / max_val

audio_int16 = np.int16(audio_float * 32767)

# Create AudioData object correctly
audio = sr.AudioData(audio_int16.tobytes(), sample_rate, 2)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Speech recognition service error:", e)
