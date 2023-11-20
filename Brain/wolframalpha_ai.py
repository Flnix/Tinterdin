import wolframalpha
from Body.Speak import Speak
from Data.apikey import wolframalpha_id

app_id = wolframalpha_id


def computational_intelligence(question,chat_log=None):
    Filelog=open("Database/Filelog.txt","r")
    chatlog_template = Filelog.read()
    Filelog.close()
    
    if chat_log is None:
        chat_log=chatlog_template
        
        try:
            prompt=f'{chat_log}You:{question}\nTinterdin:\n'
            client = wolframalpha.Client(app_id)
            answer = client.query(question)
            Answer = next(answer.results).text
            print(Answer)
        except:
            Speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
            return None
    
    chatlog_template_update=chatlog_template + f"\nYou:{question}\nTinterdin:{Answer}\n"
    Filelog=open("Database/Filelog.txt","w")
    Filelog.write(chatlog_template_update)
    Filelog.close()
    return answer
