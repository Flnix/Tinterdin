import speech_recognition as sr
import subprocess

# Create a Recognizer object
r = sr.Recognizer()

# Open a new terminal window
subprocess.run("gnome-terminal", shell=True)

# Find the window ID of the terminal window
window_id = None
while window_id is None:
    window_id = subprocess.run("xdotool search --name 'Terminal'", shell=True, stdout=subprocess.PIPE).stdout.decode().strip()

# Create a Microphone object
mic = sr.Microphone()

while True:
    # Listen for the user's voice
    print("Listening...")
    with mic as source:
        audio = r.listen(source)

    # Recognize the command
    print("Recognizing...")
    try:
        command = r.recognize_google(audio)
    except sr.UnknownValueError:
        continue

    # Activate the terminal window
    subprocess.run(f"xdotool windowactivate --sync {window_id}", shell=True)

    # Run the command in the terminal window
    subprocess.run(f"xdotool type --clearmodifiers --delay 50 '{command}'", shell=True)
   
