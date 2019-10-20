from chatterbot import ChatBot

chatbot = ChatBot(
    "Ejemplo bot",
    trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
    )

#chatbot.train(
#    "chatterbot.corpus.spanish"
#)