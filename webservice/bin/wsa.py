#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
import base64
import sqlite3
import simplejson as json

from os import listdir
from flask import Flask, request,g
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from json import dumps
from img_classifier import PictureClassifier

#export FLASK_APP=wsa.py
#python -m flask run

app = Flask(__name__)
api = Api(app)

CORS(app)


@app.route("/photos")
def get_photos():

    data = {}
    data['photos'] = []
    for photo in listdir("./photos"):
        if photo != "desktop.ini":
            image = open('./photos/'+photo, 'rb') #open binary file in read mode
            image_read = image.read()
            image_64_encode = base64.encodestring(image_read)
            sname=""
            i=photo.rfind(".")
            if(i!=0):
                n=len(photo)
                sname=photo[0:i]
            data['photos'].append({'name': sname,'path': image_64_encode})

    return jsonify(data)

@app.route("/upload", methods=['POST'])
def upload_file():

    #Recibimos la imagen
    image_file = request.files.get('image', default=None)
    if image_file:
        #Salvamos la imagen
        f = os.path.join('uploads', image_file.filename)
        image_file.save(f)

	#Pasamos la ruta al clasificador
	c = PictureClassifier()
        probs=c.predict(f)

	if probs[0][0] > 0.49:
		#Creamos la conexion a la BBDD
		miConexion=sqlite3.connect("BBDDArtBot")
		miConexion.row_factory = sqlite3.Row

		#Creamos el cursor
		miCursor = miConexion.cursor()

		#Consulta a la BBDD
		idObra=probs[0][1]

		miCursor.execute("SELECT * FROM ARTBOT WHERE ID_OBRA = ?", [idObra])

		obras = miCursor.fetchall()

		for p in obras:
			codename=p[0]
			name=p[1]
			desciption=p[2]

			#Cerramos la conexion
			miConexion.close()
			probability = 'I think the image is the %s, with %s %% of probability' % (probs[0][1], str("{0:.2f}".format(probs[0][0]*100)))      
   
			return jsonify({'code':1, 'codename':codename, 'name':name,'desciption':desciption,'probability':probability})

        return jsonify({'code':2, 'desciption':'Sorry, We can not recognize the image.','probability':'The probability is less than 50%.'})
    else:

	return jsonify({'code':0, 'message':'image file error!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')


