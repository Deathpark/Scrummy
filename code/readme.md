# Modelo para receber uma resposta do chatgpt
openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": message},
        {"role": "assistant", "content": message},
        {"role": "user", "content": message},
    ],
)

# Tipos de 'role' utilizadas pela API
## System
Sistema
## Assistant
Chatgpt
## User
Usuário

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

# Por que não usar a API do openAI?
Caso o usuário não possua uma assinatura na openAI, as requisições que podem ser feitas é extremamente baixa, tornando inviável a utilização da API para testes e treinamento do chatbot.

# NLTK 
É uma das ferramentas mais utilizadas para processamento de linguagem natural, foi desenvolvida em Python e tem uma gama muito grande de recursos, como: classificação, tokenização, stemming, tagging, parsing e raciocínio semântico. Todas essas funções são utilizadas para análise de texto;
# Numpy 
É uma biblioteca para a linguagem Python com funções para se trabalhar com computação numérica, e que pode realizar operações de álgebra linear de maneira muito eficiente;
# Tensorflow
É uma biblioteca de código aberto criada para aprendizado de máquina, computação numérica e muitas outras tarefas;
# Keras
Por último, e de extrema importância, usamos o Keras para a estrutura de aprendizado profundo, essa lib poderosíssima é uma das principais APIs de redes neurais de alto nível.

# Como rodar o chatBot treinado?
Para usar o chatbot treinado, inicialmente é necessário se certificar que a versão do python está entre 3.8 e 3.11, pois a biblioteca TenserFlow possui suporte somente para estas versões do python até o momento do desenvolvimento deste projeto.

Para verificar a versão do python, é necessário digitar o seguinte comando em seu cmd ou console do seu editor de código:
```
    python --version
```
ou
```
    py --version
```

Após certificado que a versão do python suporta o TenserFlow e todas as bibliotecas foram devidamente instaladas, e necessário treinar o chatBot com as frases pré-geradas. Para isso, usaremos o comando abaixo:
```
    python trainingChatBot.py
```
Após o comando acima ser executado com sucesso, podemos iniciar o chatbot e começar a conversação com o seguinte comando:
```
    python chatbotInterface.py
```