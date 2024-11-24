import os
from openai import OpenAI
from dotenv import dotenv_values, load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def send_message(message, chatMessages = []):
    chatMessages.append({
        {
            "role": "user", 
            "content": message
        },
    })

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = chatMessages,
    )

    return response["choices"][0]["message"]

chatMessages = []
while True:
    userText = input("Escreva seu texto aqui (Digite sair para sair)")

    if userText == "sair":
        break
    else:
        response = send_message(userText, chatMessages)
        chatMessages.append(response)
        print("Scrummy: ", response['content'])