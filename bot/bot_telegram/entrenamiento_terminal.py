# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer #method to train the chatbot
from chatterbot import ChatBot #import the chatbot

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot. Change name
chatbot = ChatBot('MuAnBot')

# Train the chat bot with a few responses
#personal life training
personalife = [
	'Who is Antonio Rodriguez Garcia',
	'He was a self-taught Asturian sculptor and painter whose career was cut short by the Civil War. Born in Candas on February 16, 1911 in the bosom of a humble family.',
	'Who is Anton',
	'He was a self-taught Asturian sculptor and painter whose career was cut short by the Civil War. Born in Candas on February 16, 1911 in the bosom of a humble family.',
	'When was born',
	'He was born in Candas on February 16, 1911',
 	'Where was he born',
 	'He was born in Candas on February 16, 1911',
 	'When did he died',
 	'In the summer of 1936 he was arrested in Candas for no reason and in May 1937 he died on the front of Murias de Candamo.',
 	'Where did he die',
	'In the summer of 1936 he was arrested in Candas for no reason and in May 1937 he died on the front of Murias de Candamo.',
	'Tell me something about his childhood',
	'This artist is born in a humble family of Candas. From an early age, he draws and molds guided by his creative instinct. He is a self-taught artist who develops in an unfavorable environment that only his iron will can overcome.',
	'Tell me something about his life',
	'This artist was born in a humble family of Candas. From an early age, he draws and molds guided by his creative instinct. He is a self-taught artist who develops in an unfavorable environment that only his iron will can overcome.',
	'Where did he study?',
	'Anton attends as a free student of the School of Fine Arts of San Fernando, the Circle of Fine Arts of Madrid and the sculpture classes of Juan Cristóbal.']

#training sculpture
sculpture = [
	'To the good man, Casa Albo',
	'Also known as The distressed worker this, sculpture was made in 1932. Location: Park of San Antonio, Candas, Asturias. Material: Bronze. Measurements: 1.62 x 0.65 x 0.56 m (also 1.54 x 0.65 x 0.54 m.)',
	'Casa Albo',
	'Also known as The distressed worker this, sculpture was made in 1932. Location: Park of San Antonio, Candas, Asturias. Material: Bronze. Measurements: 1.62 x 0.65 x 0.56 m (also 1.54 x 0.65 x 0.54 m.)',
	'The distressed worker',
	'Also known as To the good man, Casa Albo, this sculpture was made in 1932. Location: Park of San Antonio, Candas, Asturias. Material: Bronze. Measurements: 1.62 x 0.65 x 0.56 m (also 1.54 x 0.65 x 0.54 m.)',
    'Sailor',
    'This sculpture was made in 1933 Location: Paseo del Puerto, near the Hotel Marsol, Candas, Carrenio, Asturias. Material: Bronze.  Measurements: 1.35 x 0.63 x 0.59 m. (measurements of the work in wood)',
    'Portrait of Jose Fernandez',
    'Sculpture made around 1932, in Madrid',
	'Jose Gonzalez Longoria',
    'Bust of Jose Gonzalez Longoria, was made in 1935. Material: Bronze. Measurements: 37x19x25 cm.',
    'My Grandma',
    'Bust of Jose Gonzalez Longoria, was made in 1935. Material: Bronze. Measurements: 37x19x25 cm.',
	#Fin de la romeria. Bronce fundido del original en escayola
	'End of the pilgrimage',
    'This sculpture was made in 1932. Material: Molten bronze of the original in plaster.  Measurements: 76.5 x 70 x 33.5 cm.',
    'The Guaxa',
    'This sculpture was made in 1933. Material: Molten bronze of the original in plaster.  Measurements: 31 x 22.5 x 20.5 cm.',
    'Antroxu',
    'This sculpture was made in 1936. Material: Molten bronze of the original in plaster.  Measurements: 65.5 x 38 x 40 cm.']

#training painting
painting = [
	'Portrait of Goya',
	'This painting was made in 1928. Material: Oil on canvas. Measurements: 35x22 cm.',
	'Goya',
	'This painting was made in 1928. Material: Oil on canvas. Measurements: 35x22 cm.',
	'My sister Concha',
	'This painting was made in 1934. Material: Oil on canvas. Measurements: 163x98 cm.',
	'Concha',
	'This painting was made in 1934. Material: Oil on canvas. Measurements: 163x98 cm.',
	'Candas Wharf',
	'This painting was made in 1932. Material: Watercolor. This drawing was made in 1932 as a previous step to make the sculpture of The distressed worker',
	'Candas Wharf',
	'This painting was made in 1932. Material: Watercolor.']

#training drawing
drawing = [
	'Portrait of his mother',
	'This drawing was made in 1936. Pencil drawing.',
	'Sketch for a sculpture',
	'This drawing was made in 1932. ']

#training Abuse
abuse = [
	'Fool',
	'Sorry I do not answer to rudeness',
	'Cunt',
	'Sorry I do not answer to rudeness',
	'Pussy',
	'Sorry I do not answer to rudeness',
	'Whore',
	'Sorry I do not answer to rudeness',
	'Asshole',
	'Sorry I do not answer to rudeness',
	'Jerk',
	'Sorry I do not answer to rudeness',
	'Dickhead',
	'Sorry I do not answer to rudeness',
 	'Motherfucker',
 	'Sorry I do not answer to rudeness',
 	'Dumbass',
 	'Sorry I do not answer to rudeness',
 	'Fuck',
 	'Sorry I do not answer to rudeness',
	'Bollocks',
	'Sorry I do not answer to rudeness']

#set the trainer
chatbot.set_trainer(ListTrainer)
#train the bot
chatbot.train(personalife)
chatbot.train(sculpture)
chatbot.train(painting)
chatbot.train(drawing)
chatbot.train(abuse)

while True:
		request = raw_input('User:')
		response = chatbot.get_response(request)
		if float(response.confidence > 0.8):
			print ('Anton says: '+str(response))
		else:
			print ('Anton says: Sorry, I do not understand you!')


