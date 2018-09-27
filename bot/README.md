
CREAR UN CHATTERBOT

 1º Instalar y configurar python y un IDE, en mi caso elegi Atom.

 2º Instalar pip para gestionar las librerias de python:
 	$ sudo apt install python3-venv python3-pip
 	$ sudo apt install python-pip

	(Actualizar porque aunque instala chatterbot da problemas en la ejecucion)
 	$ pip install --upgrade setuptools

 3º Instalar la libreria chatterbot
 	$ pip install chatterbot

 4º Crear el bot en bot_terminal.py, y entrenarlo añadiendole un trainer para que pueda empezar a conversar.

 5º Ejecutar el archivo bot_terminal.py desde la terminal y conversar con el bot
	$ python [ruta]/bot_terminal.py

	* Aprendera de la conversacion y lo guardara (en este caso en un archivo SQLite3 que crea en la ruta especificada)

-----------------------------------------------------------
    
CREAR UN BOT EN TELEGRAM

 1º Buscar al BotFather en telegram (@BotFather)

 2º Crear el bot con /newbot o pulsando la opcion

 3º Elegir el nombre del bot

 4º Indicar el nombre de usuario del bot, que sera por el que se le encuentre cuando se le busque y que debe acabar en 'bot'.

 5º Te da una enlace donde encontrarle en Telegram y un token, que usaremos para empezar a trabajar en el.

 6º Establecer los comandos que apareceran al usuario y a los que el bot va a responder con /setcommands añadiendo una descripcion de los mismos

 7º Terminar de configurarlo con las opciones que te ofrece BotFather

-----------------------------------------------------------

CONTROLAR EL BOT

 1º Instalar la libreria de pyTelegramBotAPI:
	$ sudo pip install pyTelegramBotAPI

 2º Crear un nuevo documento (bot_telegram.py) en la misma carpeta

 3º Crear un objeto bot pasandole el token como parametro

 4º Indicarle a que comandos responder y con que metodos (ver bot_telegram.py)

 5º Ejecutar bot_telegram.py desde terminal

 6º Probar el bot en telegram enviandole los comandos que hemos programado para que responda

-----------------------------------------------------------

ENLAZAR CON EL CHATTERBOT

 1º En bot_telegram.py creo una funcion para enviar una peticion al chatterbot. Para ello lo creo igual que en bot_terminal.py, pero sin establecer la entrada y salida de datos por el terminal y entrenandole solo en la primera ejecucion del script.

 2º Paso el mensaje del usuario a la funcion y obtengo la respuesta del chatterbot que guardo en una variable

 3º Creo un archivo de texto para guardar la respuesta temporalmente

 4º Leo el archivo con la respuesta y se la paso al bot de telegram para que la devuelva

 *Cuidado con cualquier simbolo extraño (caracteres especiales, tildes, ñ). En terminal no hay problema, pero en telegram rompe cuando el bot los tiene que enviar como respuesta.





















