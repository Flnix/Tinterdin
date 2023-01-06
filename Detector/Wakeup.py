import os
import speech_recognition as sr
from Body.Speak import Speak

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source) 
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""
    
    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():
    
    while True:

        query = Listen()
        if "activate the machine"in query:
            Speak("Access Granted")
            return True
        
        elif "retry" in query:
            pass  # allow the user to retry the password
        else:
            Speak("Incorrect password. Please try again.")
