
from fastapi import FastAPI
from flask import Flask,request,redirect,url_for
from flasgger import Swagger
import pickle
import pandas as pd
import json
app = FastAPI()
"""
	Requirement txt not working and bash command from pyenv neither can't see what am i doing
"""

# define a root `/` endpoint
@app.get("/")
def index():
    return redirect(url_for('flasgger.apidocs'))

@app.get("/predict",method=['GET'])
def prediction():

	"""
	parameters
	"""
	if acousticness not in request.args:
		acousticness = 0
	else:
		acousticness = float(request.args['acousticness'])

	if danceability not in request.args:
		danceability = 0
	else:
		danceability = float(request.args['danceability'])

	if duration_ms not in request.args:
		duration_ms = 0
	else:
		duration_ms = int(request.args['duration_ms'])

	if energy not in request.args:
		energy = 0
	else:
		energy = float(request.args['energy'])

	if explicit not in request.args:
		explicit = 0
	else:
		explicit = int(request.args['explicit'])

	if str(id) not in request.args:
		id = "0"
	else:
		id = str(request.args['id'])

	if instrumentalness not in request.args:
		instrumentalness = 0
	else:
		instrumentalness = float(request.args['instrumentalness'])

	if key not in request.args:
		key = 0
	else:
		key = int(request.args['key'])

	if liveness not in request.args:
		liveness = 0
	else:
		liveness = float(request.args['liveness'])

	if loudness not in request.args:
		loudness = 0
	else:
		loudness = float(request.args['loudness'])

	if mode not in request.args:
		mode = 0
	else:
		mode = int(request.args['mode'])

	if name not in request.args:
		name = "0"
	else:
		name = str(request.args['name'])

	if release_date not in request.args:
		release_date = "0"
	else:
		release_date = str(request.args['release_date'])

	if speechiness not in request.args:
		speechiness = 0
	else:
		speechiness = float(request.args['speechiness'])

	if tempo not in request.args:
		tempo = 0
	else:
		tempo = float(request.args['tempo'])

	if valence not in request.args:
		valence = 0
	else:
		valence = float(request.args['valence'])

	if artist not in request.args:
		artist = "0"
	else:
		artist = str(request.args['artist'])
	d= {'acousticness':acousticness,'danceability':danceability,'duration_ms':duration_ms,'energy':energy,'explicit':explicit,'id':id,'instrumentalness':instrumentalness,'key':key,'liveness':liveness,'loudness':loudness,'mode':mode,'name':name,'release_date':release_date,'speechiness':speechiness,'tempo':tempo,'valence':valence,'artist':artist}

	pd.DataFrame(data = d)

	popularity = loaded_model.predict(d)
	dico = {"artist": artist,"name": name,"popularity": popularity}
	return app.response_class(
		response = json.dumps(dico),
		status = 200,
		mimetype = 'applicaation/json'
		)

# Implement a /predict endpoint
loaded_model = pickle.load(open(filename, '../model.joblib'))