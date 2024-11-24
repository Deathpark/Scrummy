model to recieve answer from chatgpt
openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": message},
        {"role": "assistant", "content": message},
        {"role": "user", "content": message},
    ],
)

## System = system
## Assistant = chatgpt
## User = user