from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Armando')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.spanish")

request = ""
while request!="salir":
    request = input("Tu: ")
    response = chatbot.get_response(request)
    print("Bot: ", response)