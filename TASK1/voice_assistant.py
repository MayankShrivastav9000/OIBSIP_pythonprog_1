import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize engines
recognizer = sr.Recognizer()
#engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)

    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def listen(duration=5):
    sample_rate = 16000

    print("Listening...")
    audio_float = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    audio_float = np.squeeze(audio_float)

    max_val = np.max(np.abs(audio_float))
    if max_val > 0:
        audio_float = audio_float / max_val

    audio_int16 = np.int16(audio_float * 32767)
    audio = sr.AudioData(audio_int16.tobytes(), sample_rate, 2)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("I did not understand that")
        return ""
    except sr.RequestError:
        speak("Speech service error")
        return ""

def process_command(command):
    if "hello" in command:
        speak("Hello, how can I help you")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        speak("What should I search for")
        query = listen()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        exit()

    else:
        speak("Command not recognized")

# Main loop
speak("Voice assistant started")

while True:
    command = listen()
    if command:
        process_command(command)


#py -3.11 voice_assistant.py