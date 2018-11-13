import os
from os.path import exists
import time
import logging
import telebot
from chatterbot import ChatBot


# LOAD USERS LIST
users = list()
for line in open('users.txt','r'):
    id = int(line)
    users.append(id)


# READ THE TOKEN
token = ''
if exists('token.txt'):
    with open('token.txt') as file:
        token = file.readline().strip()
    print('Token loaded')
else:
    print('No token file detected')


# LINK THE BOT WITH TELEGRAM USING THE TOKEN
telegram_bot = telebot.TeleBot(token)

logger = telebot.logger
logging.basicConfig(level=logging.ERROR)


# CREATE THE CHATBOT
chatbot = ChatBot("MuseoAntonBot",
        # STORAGE
        storage_adapter = "chatterbot.storage.SQLStorageAdapter",
        database = "bot_telegram.sqlite3",
        # LOGIC
	    logic_adapters=[
            "chatterbot.logic.BestMatch",
	        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
            }
        ],
        # INPUT
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace',
            'chatterbot.preprocessors.convert_to_ascii'
        ],
        # LEARNING
        trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
    )

# CHATBOT TRAINING
# FIND OUT WHY DOES NOT LOAD THE WHOLE FOLDER
#chatbot.train(
#    "chatterbot.corpus.english",
#    "chatterbot.corpus.custom"
#    )

# EXPORT THE TRAINING
# chatbot.trainer.export_for_training('./trained.yml')


# BROADCAST
def broadcast(message_to_send):
    for user in users:
        telegram_bot.send_message(user, message_to_send)


# LISTENERS FOR COMMANDS
@telegram_bot.message_handler(commands=['start'])
def start_response(message):
    if message.chat.id not in users:
        telegram_bot.send_message(message.chat.id, "Welcome to the Anton Museum <b>" +
        message.from_user.first_name + "</b>!", parse_mode="HTML")
        users.append(message.chat.id)
        with open('users.txt','a') as f:
            f.write(str(message.chat.id)+'\n')
    else:
	   telegram_bot.send_message(message.chat.id, "Welcome back to the Anton Museum <b>" +
       message.from_user.first_name + "</b>!", parse_mode="HTML")

@telegram_bot.message_handler(commands=['help'])
def help_response(message):
	telegram_bot.send_message(message.chat.id, "I am here to help you")

@telegram_bot.message_handler(commands=['web'])
def web_response(message):
	telegram_bot.send_message(message.chat.id, "<a href='http://museoanton.com/'>Click here</a>", parse_mode="HTML")

# WORK IN PROGRESS
#@telegram_bot.message_handler(commands=['logo'])
#def web_response(message):
#    image = 'profile_pictures/BotPic.jpeg'
#    if exists(image):
        



# LISTENER FOR IMAGES
# AS A DOCUMENT
@telegram_bot.message_handler(func=lambda message: message.document.mime_type.startswith('image/'), content_types=['document'])
def handle_image_as_document(message):
    telegram_bot.send_message(message.chat.id, "I received your image as a document")
    resend_image(message)

# AS A PHOTO
@telegram_bot.message_handler(content_types=['photo'])
def handle_image_as_photo(message):
    telegram_bot.send_message(message.chat.id, "I received your image as a photo")
    resend_image(message)

# SAVE THE IMAGE AND SEND IT BACK
def resend_image(message):
    # Search the biggest photo (avoid thumbnails)
    image_file_id = None
    base_size = 0
    for photo in message.photo:
        total_size = photo.height * photo.width
        if total_size > base_size:
            base_size = total_size
            image_file_id = photo.file_id

    # Download and write the file
    file_info = telegram_bot.get_file(image_file_id)
    file_download = telegram_bot.download_file(file_info.file_path)

    # file_download is something like this:
    # https://api.telegram.org/file/bot<token>/<file_path>

    with open(image_file_id, 'wb') as file:
        file.write(file_download)

    # Send "uploading photo" action since can take a few seconds
    telegram_bot.send_chat_action(message.chat.id, 'upload_photo')

    # Upload the photo and do it as a reply
    telegram_bot.send_photo(message.chat.id,
                   open(image_file_id, 'rb'),
                   caption= "Your image")
    try:
        os.unlink(image_file_id)
    except Exception as err:
        logger.error(err)


# GENERIC LISTENER
@telegram_bot.message_handler(func=lambda message:True)
def answer_telegram(message):
    if message.content_type == 'text':
        if message.text == 'Broadcast':
            broadcast('Broadcaaaaaast!')
        else:
            telegram_bot.send_chat_action(message.chat.id, 'typing')
            ask_chatterbot(message.text)
            response = open("response.txt", "r")
            response = response.read()
            telegram_bot.send_message(message.chat.id, response)


# ASK TO THE CHATTERBOT
def ask_chatterbot(message):
    response = chatbot.get_response(message)
    response = str(response)

    resp_file = open("response.txt", "w")
    resp_file.write(response)
    resp_file.close()


#Send Sculptor main work
#@telegram_bot.message_handler(func=lambda message:True)
#def send_image(self, message):
#	response = 'ruta'
#	for palabra in listaR:
#		if message.find(palabra, beg=0, end=len(string)):
#		    if os.path.exists(file_image):
#				telegram_bot.reply_to(message,content_type='photo', response)
#listaR = ['favorite', 'important','principal']


# KEEP THE BOT LISTENING TO TRY THE BOT NOT STOPPING
while True:
    try:
        telegram_bot.polling(none_stop=True)
    except Exception as err:
        logger.error(err)
        time.sleep(10)
