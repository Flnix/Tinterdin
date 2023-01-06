import openai
from dotenv import load_dotenv
from Data.apikey import openai_apikey

openai.api_key= openai_apikey
load_dotenv()
completion=openai.Completion(openai_apikey)

def Reply(question,chat_log=None):
    Filelog=open("Database/Filelog.txt","r")
    chatlog_template = Filelog.read()
    Filelog.close()
    
    if chat_log is None:
        chat_log=chatlog_template
    
    prompt=f'{chat_log}You:{question}\nTinterdin:\n'
    response= completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=1,
        max_tokens=100,
        top_p=0.0,
        frequency_penalty=0.0,
        presence_penalty=1
    )
    if not response.choices:
        # The list is empty
        answer = "I'm sorry, I am unable to generate a response at this time."
    elif response.choices[0].text is None:
    # The text field is null
        answer = "I'm sorry, I am unable to generate a response at this time."
    else:
    # The text field is not null
        answer = response.choices[0].text.strip()

    answer=response.choices[0].text.strip()
    chatlog_template_update=chatlog_template + f"\nYou:{question}\nTinterdin:{answer}\n"
    Filelog=open("Database/Filelog.txt","w")
    Filelog.write(chatlog_template_update)
    Filelog.close()
    return answer



    