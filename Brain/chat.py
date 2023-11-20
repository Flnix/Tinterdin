import aiml

AIML = aiml.Kernel()

try:
    AIML.loadBrain("tinterdin.Data")
except:
    print("Failed to load brain file. Loading AIML files...")
    AIML.learn("Database/*")
    AIML.saveBrain("tinterdin.Data")
    AIML.loadBrain("tinterdin.Data")

def Reply(question):
    # Assuming you want to read the chat log each time and append the new conversation
    with open("DataBase/Filelog.txt", "a") as filelog:
        filelog.write(f"You: {question}\n")

    input_text = question.upper()
    response = AIML.respond(input_text)
    
    if not response:
        print(f"I'm sorry, I am unable to generate a response at this time. {input_text}")
    else:
        print(f"Tinterdin: {response}")

    answer = response.strip()

    # Assuming you want to update the chat log with the response
    with open("DataBase/Filelog.txt", "a") as filelog:
        filelog.write(f"Tinterdin: {answer}\n")

    return answer


