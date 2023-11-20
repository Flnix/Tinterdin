# Tinterdin
# A Currently developing AI Simplar to Jarvis (In IronMan)
- Greet user
- Tells current time and date
- Launch applications/software 
- Open any website
- Tells about the weather of any city
- Open the location of any place plus tell the distance between your place and the queried place
- Tells your current system status (RAM Usage, battery health, CPU usage)
- Tells about your upcoming events (Google Calendar)
- Tells about any person (via Wikipedia)
- Can search for anything on Google 
- Can play any song on YouTube
- Tells top headlines (via Times of India)
- Plays music
- Send email (with subject and content)
- Calculate any mathematical expression (example:calculate x + 135 - 234 = 345)
- Answer any generic question (via WolframAlpha)
- Take important notes in a notepad
- Tells a random joke
- Sends SOS message along with the current location to your registered mobile number
- Tell your IP address
- Can switch the window
- Can take screenshots and save them with a custom filename
- Can hide all files in a folder and also make them visible again
- Currently Developing Tinterdin to perform Hacking Stuff.


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
- Navigate to the directory of your project
- Install all the requirements by just hitting ``` pip install -r requirements.txt ```
- Install PyAudio from the wheel file by following the instructions given [here](https://stackoverflow.com/a/55630212)
- Run the program by ``` python Tinterdin.py ```
- Enjoy !!!!

## Code Structure
 
    ├── Body                # Contains Listen and Speak Function
    ├── Brain               # All functionalities of Tinterdin
    ├── Data                # All Api && Secret keys
    ├── Database            # Contains the chat logs
    ├── DataBase            #Contains the Datas for the Tinterdin
    ├── Detector            # Contains Clap && Command Wakeup Function
    ├── driver              # Contain ChromeWebDriver
    ├── Tinterdin.py        # main driver program of Tinterdin
    ├── requirements.txt    # all dependencies of the program
    ├── README.md           # This file


