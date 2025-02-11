'''
  esse é o arquivo de configuração que captura a expressão de ativação, faz a
  conversão da voz do usuário em texto (técnica de SPEECH-TO-TEXT), e
  posteriormente faz a tradução da resposta em texto do chatbot para uma
  reprodução de áudio (técnica TEXT-TO-SPEECH)
'''

# import the libraries
import speech_recognition as sr

import os
from gtts import gTTS
import warnings

import random

from pygame import mixer
from constants import *


# ignorar qualquer mensagem a nível de WARNING
warnings.filterwarnings('ignore')


# grava áudio e devolve como texto (speech-to-text)
def recordAudio():
    # grava o áudio
    r = sr.Recognizer()  # criando um objeto de reconhecimento

    # abre o microfone e começa a gravação
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Diga algo...")
        audio = r.listen(source)

    # chama o reconhecimento de fala do Google
    data = ''
    try:
        data = r.recognize_google(audio, language=LANG_PT_BR)
        print('Você disse \"' + data + '\"')
    except sr.UnknownValueError:  # exceção para tratar erros desconhecidos
        print('Reconhecimento de fala do Google não pôde entender o seu áudio, erro desconhecido')
    except sr.RequestError as e: # exceção para erros gerais
        print('O reconhecimento de fala do Google gerou um erro: ' + e)

    return data


# gerar resposta de áudio com base no texto (text-to-speech)
def chatbotResponse(text):
    try:
        # verifica se o mixer está inicializado antes de tentar parar ou descarregar
        if mixer.get_init():
            if mixer.music.get_busy():
                mixer.music.stop()
            mixer.quit()

        # remove o arquivo de áudio antigo, se existir
        if os.path.exists('chatbot_response.mp3'):
            os.remove('chatbot_response.mp3')
    except PermissionError:
        print('Erro de permissão para apagar o arquivo')

    print(text)

    # converte o texto em fala
    if text == '':
        print('Não há texto para converter')
        return

    myobj = gTTS(text=text, lang=LANG_PT_BR, slow=False)

    # salvar o áudio convertido em um arquivo
    audioName = 'chatbot_response.mp3'
    myobj.save(audioName)

    # tocar o áudio convertido
    mixer.init()
    mixer.music.load(audioName)
    mixer.music.play(fade_ms=200)
    return


# função para buscar pelas expressões de ativação (wake-words)
def wakeWord(text):

    text = text.lower()  # converte o texto para minúsculas

    # verificar se a fala do usuário contém palavras de ativação
    for phrase in WAKE_WORDS:
        if phrase in text:
            chatbotResponse(random.choice(WAKE_WORDS_RESPONSE) + '.')
            return True

    # se não há palavras de ativação na fala do usuário, retorna
    return False


while True:
    print("Aguardando comando de ativação")

    # grava o comando do usuário
    wakeCommand = recordAudio()
    response = ''

    # busca por comandos de ativação
    if wakeWord(wakeCommand):
        message = recordAudio()

        if 'obrigado' in message:
            response = response + 'de nada'

        # resposta do chatbot
        chatbotResponse(response)

    if response == '':
        response = "Não foi possível encontrar comandos de ativação"
    print(response)


chatbotResponse(message)
