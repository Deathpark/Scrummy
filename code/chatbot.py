import os
from openai import OpenAI
from dotenv import dotenv_values, load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def send_message(message):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "user", 
                "content": message
            },
        ],
    )

    return response["choices"][0]["message"]

print(send_message("Em que ano estamos?"))