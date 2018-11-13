from chatterbot import ChatBot

# CREATE BOT
chatbot = ChatBot(

    "Bot_terminal",

    storage_adapter = "chatterbot.storage.SQLStorageAdapter",
    database = "./bot_terminal.sqlite3",

    input_adapter = "chatterbot.input.TerminalAdapter",
    output_adapter = "chatterbot.output.TerminalAdapter",

    trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
    )

# TRAIN ONLY THE FIRST TIME
# chatbot.train("chatterbot.corpus.english")

print("Start chatting:")

while True:
    try:
        bot_input = chatbot.get_response(None)

    # EXIT WITH Ctrl+c
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
