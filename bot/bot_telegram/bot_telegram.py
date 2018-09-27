import telebot
from chatterbot import ChatBot


# ENLAZAR EL BOT MEDIANTE EL TOKEN 
# (cambiar 'TOKEN' por el token del bot)
telegram_bot = telebot.TeleBot("TOKEN")

# INDICAR A QUE COMANDOS RESPONDER Y CON QUE FUNCION
@telegram_bot.message_handler(commands=['start'])
def start_response(message):
	telegram_bot.reply_to(message, "Bienvenido al Museo Anton")

@telegram_bot.message_handler(commands=['help'])
def help_response(message):
	telegram_bot.reply_to(message, "Estoy aqui para ayudarte")

@telegram_bot.message_handler(commands=['web_museo'])
def give_response(message):
	telegram_bot.reply_to(message, "http://museoanton.com/")


# CREAR UNA FUNCION PARA QUE EJECUTE EL CHATTERBOT
def preguntar_chatterbot(message):
    #CREAR EL CHATBOT
    chatbot = ChatBot("MuseoAntonBot",
        # ALMACENAMIENTO
        storage_adapter = "chatterbot.storage.SQLStorageAdapter",
        database = "./bot_telegram.sqlite3",
        # APRENDIZAJE
        trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
    )

    # ENTRENARLO SOLO LA PRIMERA VEZ
    chatbot.train("chatterbot.corpus.spanish")

    # OBTENER LA RESPUESTA DEL CHATBOT
    response = chatbot.get_response(message)
    response = str(response)

    # ALMACENO LA RESPUESTA EN UN ARCHIVO
    resp_file = open("response.txt", "w")
    resp_file.write(response)
    resp_file.close()



# LLAMADA AL CHATTERBOT AL ENTRAR MENSAJE DIFERENTE DE LOS COMANDOS ESTABLECIDOS
@telegram_bot.message_handler(func=lambda message:True)
def contestar_telegram(message):
    preguntar_chatterbot(message.text)

    # LEO LA RESPUESTA DEL ARCHIVO
    response = open("response.txt", "r")
    response = response.read()

    # MANDAR LA RESPUESTA AL BOT DE TELEGRAM PARA QUE CONTESTE
    telegram_bot.reply_to(message, response)



# MANTIENE EL BOT ABIERTO A LA ESPERA DE MENSAJES
telegram_bot.polling()
