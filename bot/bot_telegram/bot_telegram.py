
import telebot
from telebot import apihelper.logger
from chatterbot import ChatBot

# LINK THE BOT USING THE TOKEN

telegram_bot = telebot.TeleBot("625012255:AAEMDEXQqhoYKP5cbeMjjzdO9j1rGq_7FT4")


# SET FUNCTIONS TO RESPONSE TO THE COMMANDS 
@telegram_bot.message_handler(commands=['start'])
def start_response(message):
	telegram_bot.reply_to(message, "Welcome to the Anton Museum")

@telegram_bot.message_handler(commands=['help'])
def help_response(message):
	telegram_bot.reply_to(message, "I am here to help you")

@telegram_bot.message_handler(commands=['web'])
def web_response(message):
	telegram_bot.reply_to(message, "http://museoanton.com/")


# NEW FUNCTION TO CREATE THE CHATTERBOT
def ask_chatterbot(message):
    chatbot = ChatBot("MuseoAntonBot",
        # STORAGE
        storage_adapter = "chatterbot.storage.SQLStorageAdapter",
        database = "bot_telegram.sqlite3",
        # LEARNING
        trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
    )

    #(ONLY THE FIRST TIME)
    # chatbot.train("chatterbot.corpus.english")

    response = chatbot.get_response(message)
    response = str(response)

    resp_file = open("response.txt", "w")
    resp_file.write(response)
    resp_file.close()


# SEND THE RESPONSE TO TELEGRAM
@telegram_bot.message_handler(func=lambda message:True)
def answer_telegram(message):
    ask_chatterbot(message.text)

    response = open("response.txt", "r")
    response = response.read()

    telegram_bot.reply_to(message, response)


# KEEP THE BOT LISTENING TO TRY THE BOT NOT STOPPING
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as err:
        logger.error(err)
        time.sleep(5)

        

