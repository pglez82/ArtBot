import logging
import telebot 
from chatterbot import ChatBot


# LINK THE BOT USING THE TOKEN
telegram_bot = telebot.TeleBot("TOKEN")

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

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

'''# SEND A IMAGE
def send_image(self, file_image):
    if os.path.exists(file_image):
        super(MuseoAntonBot, self).sendPhoto(chat_id=self.channel_id,
                                         photo=open(file_image, 'rb'))'''



# KEEP THE BOT LISTENING TO TRY THE BOT NOT STOPPING
while True:
    try:
        telegram_bot.polling(none_stop=True)
    except Exception as err:
        logger.error(err)
        time.sleep(5)
        

'''# Either set logger like: 
   logger = logging.getLogger(__name__)

# or use logging instead:

    logging.info('Generic on file {} starts at {}'.format(file_path , time.time()))'''

'''otra opción, meterlo en una base de datos y leerlo
chatbot.train(
	"./data/greetings_corpus/custom.corpus.json",
	"./data/my_corpus/"
	)'''