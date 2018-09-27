from chatterbot import ChatBot

# CREACION BOT
chatbot = ChatBot(

    "Bot_terminal",

    # ALMACENAMIENTO
    storage_adapter = "chatterbot.storage.SQLStorageAdapter",
    database = "./bot_terminal.sqlite3",

    # ENTRADA Y SALIDA
    input_adapter = "chatterbot.input.TerminalAdapter",
    output_adapter = "chatterbot.output.TerminalAdapter",

    # APRENDIZAJE
    trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
    )

# ENTRENAMIENTO 
#(comentar despues de la primera vez)
chatbot.train("chatterbot.corpus.spanish")

print("Empieza la conversacion:")

# CONVERSACION EN BUCLE
while True:
    try:
        bot_input = chatbot.get_response(None)

    # SALIR CON Ctrl+c
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
