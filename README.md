# Tinterdin
# A Currently developing AI Simplar to Jarvis (In IronMan)
# Currently Developing Tinterdin to perform Hacking Stuffs.
- Greet user
- Tell current time and date
- Launch applications/softwares 
- Open any website
- Tells about weather of any city
- Open location of any place plus tells the distance between your place and queried place
- Tells your current system status (RAM Usage, battery health, CPU usage)
- Tells about your upcoming events (Google Calendar)
- Tells about any person (via Wikipedia)
- Can search anything on Google 
- Can play any song on YouTube
- Tells top headlines (via Times of India)
- Plays music
- Send email (with subject and content)
- Calculate any mathematical expression (example: Jarvis, calculate x + 135 - 234 = 345)
- Answer any generic question (via Wolframalpha)
- Take important note in notepad
- Tells a random joke
- Tells your IP address
- Can switch the window
- Can take screenshot and save it with custom filename
- Can hide all files in a folder and also make them visible again
- Has a cool Graphical User Interface

## API Keys
To run this program you will require a bunch of API keys. Register your API key by clicking the following links

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Wolframalpha](https://www.wolframalpha.com/)
- [Google Calendar API](https://developers.google.com/calendar/auth)
  
## Installation

- First clone the repo
- Change the values in the apikey.py file:
    ```weather_api_key = "<your_api_key>"
    email = "<your_email>"
    email_password = "<your_email_password>"
    wolframalpha_id = "<your_wolframalpha_id>"
- Copy the config.py file in Jarvis>config folder
- Navigate to the directory of your project
- Install all the requirements by just hitting ``` pip install -r requirements.txt ```
- Install PyAudio from wheel file by following instructions given [here](https://stackoverflow.com/a/55630212)
- Run the program by ``` python Tinterdin.py ```
- Enjoy !!!!

## Code Structure
 
    ├── Body                # Contains Listen and Speak Function
    ├── Brain               # All functionalities of Tinterdin
    ├── Data                # All Api && Secret keys
    ├── Database            # Contains the chat logs produced by OpenAI
    ├── Detector            # Contains Clap && Command Wakeup Function
    ├── driver              # Contain ChromeWebDriver
    ├── Tinterdin.py        # main driver program of Jarvis
    ├── requirements.txt    # all dependencies of the program
    ├── README.md           # This file


