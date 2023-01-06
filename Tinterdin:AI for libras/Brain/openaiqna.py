import openai
from dotenv import load_dotenv
from Data.apikey import openai_apikey

openai.api_key= openai_apikey
load_dotenv()
completion=openai.Completion()

def QutionsReply(question,chat_log=None):
    Filelog=open("Database/qna_log.txt","r")
    chatlog_template = Filelog.read()
    Filelog.close()
    
    if chat_log is None:
        chat_log=chatlog_template
    
    prompt=f'{chat_log}Ques:{question} \n Ans:\n'
    response= completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer=response.choices[0].text.strip()
    chatlog_template_update=chatlog_template + f"\nQues:{question}\nAns:{answer}\n"
    Filelog=open("Database/qna_log.txt","w")
    Filelog.write(chatlog_template_update)
    Filelog.close()
    return answer
