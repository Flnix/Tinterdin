import pyttsx3


def Speak(Text):
     try:
          engine = pyttsx3.init()
          voices = engine.getProperty('voices')
          engine.setProperty('voices','ta')
          engine.setProperty('rate', 144)
          engine.setProperty('pitch',700)
          print("")
          print(f"Tinterdin : {Text}.")
          print("")
          engine.say(Text)
          engine.runAndWait()
     except:
            t = "Sorry I couldn't understand and handle this input"
            print(t)
            return False
