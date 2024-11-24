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

# Imports Necessários
Python 3.11 requerido

pip install pyaudio
pip install SpeechRecognition
pip install gTTS
pip install wikipedia
pip install pygame
pip install openai
pip install python-dotenv
pip install nltk
pip install numpy
pip install keras
pip install tensorflow

# NLTK 
É uma das ferramentas mais utilizadas para processamento de linguagem natural, foi desenvolvida em Python e tem uma gama muito grande de recursos, como: classificação, tokenização, stemming, tagging, parsing e raciocínio semântico. Todas essas funções são utilizadas para análise de texto;
# Numpy 
É uma biblioteca para a linguagem Python com funções para se trabalhar com computação numérica, e que pode realizar operações de álgebra linear de maneira muito eficiente;
# Tensorflow
É uma biblioteca de código aberto criada para aprendizado de máquina, computação numérica e muitas outras tarefas;
# Keras
Por último, e de extrema importância, usamos o Keras para a estrutura de aprendizado profundo, essa lib poderosíssima é uma das principais APIs de redes neurais de alto nível.