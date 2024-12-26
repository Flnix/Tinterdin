import os
import sys
import subprocess
import re
import random
import pprint
import datetime
import requests
import sys
import urllib.parse  
import pyjokes
import time
import pywhatkit

from Brain.chat import Reply
from Body.Listen import Listen
from Body.Speak import Speak
from Detector.Clap import Tester
from Detector.Wakeup import WakeupDetected
from Brain.predefinedcmts import GREETINGS, GREETINGS_RES, EMAIL_DIC, CALENDAR_STRS
from Brain.date_time import Date
from Brain.date_time import Time
from Brain.launch_app import launch_app
from Brain.sos import send_sos
from Brain.sos import rescue
from Brain.website_open import website_opener
from Brain.weather import fetch_weather
from Brain.wikipedia import tell_me_about
from Brain.news import get_news
from Brain.send_email import mail
from Brain.google_search import google_search
from Brain.google_calendar import authenticate_google
from Brain.google_calendar import get_date
from Brain.google_calendar import get_events
from Brain.note import note
from Brain.system_stats import system_stats
from Brain.loc import my_location
from Brain.loc import loc
from Data.apikey import email, email_password
from Brain.wolframalpha_ai import computational_intelligence


def MainExe():
    while True:
        try:
            Speak("Initializing Tinterdin")
            print("Done")
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<=12:
                Speak("Good Morning Sir")
            elif hour>12 and hour<18:
                Speak("Good afternoon Sir")
            else:
                Speak("Good evening Sir")
                
            Speak("How can I help you, Sir!")
        
            while True:
                Data=Listen()
                Data=str(Data)
                if "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
                    Response = Reply(Data)
                    Speak(Response)
                
                elif "tell me the date" in Data:
                    Response=Date()
                    Speak(Response)
                    
                elif "what's the time"in Data or "tell me the time" in Data:
                    Respond=Time()
                    Speak(Respond)                
                
                elif "calculate" in Data :
                    question= Data
                    Response = computational_intelligence(question)
                    Speak(Response)
                    
                    '''elif "play music" in Data or "hit some music" in Data:
                    music_dir = "F://Songs//Imagine_Dragons"
                    songs = os.listdir(music_dir)
                    for song in songs:
                        os.startfile(os.path.join(music_dir, song))'''
                    
                elif re.search('open', Data):
                    domain = Data.split(' ')[-1]
                    open_result = website_opener(domain)
                    Speak(f'Alright sir, Opening {domain}')
                    print(open_result)
                    
                elif 'youtube' in Data:
                    video = Data.split(' ')[1]
                    Speak(f"Okay sir, playing {video} on youtube")
                    pywhatkit.playonyt(video)

                elif "help help" in Data:
                    send_sos(phone_number="your sos number")
                    Speak(rescue())

                elif "email" in Data or "send email" in Data or "compose a mail" in Data:
                    sender_email = email
                    sender_password = email_password
                    try:
                        Speak("Whom do you want to email sir ?")
                        recipient = Listen()
                        receiver_email = EMAIL_DIC.get(recipient)
                        if receiver_email:

                            Speak("What is the subject sir ?")
                            subject = Listen()
                            Speak("What should I say?")
                            message = Listen
                            msg = 'Subject: {}\n\n{}'.format(subject, message)
                            mail(sender_email, sender_password,receiver_email, msg)
                            Speak("Email has been successfully sent")
                            time.sleep(2)

                        else:
                            Speak("I coudn't find the requested person's email in my database. Please try again with a different name")

                    except:
                        Speak("Sorry sir. Couldn't send your mail. Please try again")
                        
                elif re.search('weather', Data):
                    city = Data.split(' ')[-1]
                    weather_res = fetch_weather(city=city)
                    print(weather_res)
                    Speak(weather_res)
                    
                elif 'search google for' in Data:
                    google_search(Data)
                    
                elif "buzzing" in Data or "news" in Data or "headlines" in Data:
                    news_res = get_news()
                    Speak('Source: The Times Of India')
                    Speak('Todays Headlines are..')
                    for index, articles in enumerate(news_res):
                        pprint.pprint(articles['title'])
                        Speak(articles['title'])
                        break
                    Speak('These were the top headlines, Have a nice day Sir..')

                elif re.search('tell me about', Data):
                    topic = Data.split(' ')[-1]
                    if topic:
                        wiki_res = tell_me_about(topic)
                        print(wiki_res)
                        Speak(wiki_res)
                    else:
                        Speak("Sorry sir. I couldn't load your query from my database. Please try again")
                            
                    '''elif "take screenshot" in Data or "take a screenshot" in Data or "capture the screen" in Data:
                    Speak("By what name do you want to save the screenshot?")
                    name = Listen()
                    Speak("Alright sir, taking the screenshot")
                    img = pyautogui.screenshot()
                    name = f"{name}.png"
                    img.save(name)
                    Speak("The screenshot has been succesfully captured")'''
                    
                    
                elif "joke" in Data:
                    joke = pyjokes.get_joke()
                    print(joke)
                    Speak(joke)   
                    
                elif "calculate" in Data:
                    question = Data
                    answer = computational_intelligence(question)
                    Speak(answer)
                                     
                elif "where i am" in Data or "current location" in Data or "where am i" in Data:
                    try:
                        city, state, country = my_location()
                        print(city, state, country)
                        Speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                    except Exception as e:
                        Speak("Sorry sir, I coundn't fetch your current location. Please try again")
                        
                    '''elif "switch the window" in Data or "switch window" in Data:
                    Speak("Okay sir, Switching the window")
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")'''
                    
                elif "ip address" in Data:
                    ip = requests.get('https://api.ipify.org').text
                    print(ip)
                    Speak(f"Your ip address is {ip}")
                    
                elif "system" in Data:
                    sys_info = system_stats()
                    print(sys_info)
                    Speak(sys_info)
                    
                elif "where is" in Data:
                    place = Data.split('where is ', 1)[1]
                    current_loc, target_loc, distance = loc(place)
                    city = target_loc.get('city', '')
                    state = target_loc.get('state', '')
                    country = target_loc.get('country', '')
                    time.sleep(1)
                    try:

                        if city:
                            res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                            print(res)
                            Speak(res)

                        else:
                            res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                            print(res)
                            Speak(res)

                    except:
                        res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                        Speak(res) 
                    
                elif "hide all files" in Data or "hide this folder" in Data:
                    os.system("attrib +h /s /d")
                    Speak("Sir, all the files in this folder are now hidden")

                elif "visible" in Data or "make files visible" in Data:
                    os.system("attrib -h /s /d")
                    Speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")
                    
                elif "goodbye" in Data or "offline" in Data or "bye" in Data or "shutdown the machine" in Data:
                    Speak("Alright sir, going offline. It was nice working with you")
                    sys.exit()
                    
                else:
                    Response=Reply(Data)
                    Speak(Response)
            
        except:
            os.execvp("python3", ["python3", "Tinterdin.py"])

def Password_checker():
        if WakeupDetected():
            MainExe()
        

        
def ClapTest():
        query= Tester()
        if "True-Mic" in query:
            Password_checker()
        else:
            pass

ClapTest()
