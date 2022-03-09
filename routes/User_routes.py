from flask import Blueprint, jsonify, request
import json
import requests
from googletrans import Translator

from models.User import User
from utils.db import db
from schemas.User_schema import User_schema

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/api/user', methods=['POST'])
def save_user():
	request_body = request.json
	new_user = User(
		request_body['nombre'], 
		request_body['apellido'], 
		request_body['email']
	)
	db.session.add(new_user)
	db.session.commit()
	user_schema = User_schema()
	return user_schema.jsonify(new_user)

@user_routes.route('/api/users', methods=['GET'])
def get_users():
	all_users = User.query.all()
	users_schema = User_schema(many=True)
	result = users_schema.dump(all_users)
	return jsonify(result)

@user_routes.route('/api/user/<int:id>', methods=['GET'])
def get_user(id):
	user = User.query.get(id)
	if(user is None):
		return jsonify({'message': 'User not found'}), 404

	user_schema = User_schema()
	return user_schema.jsonify(user)

@user_routes.route('/api/user/<int:id>', methods=['PUT'])
def update_user(id):
	user = User.query.get(id)
	if(user is None):
		return jsonify({'message': 'User not found'}), 404

	request_body = request.json
	user.nombre = request_body['nombre']
	user.apellido = request_body['apellido']
	user.email = request_body['email']
	db.session.commit()
	user_schema = User_schema()
	return user_schema.jsonify(user)

@user_routes.route('/api/user/<int:id>', methods=['DELETE'])
def delete_user(id):
	user = User.query.get(id)
	if(user is None):
		return jsonify({'message': 'User not found'}), 404
		
	db.session.delete(user)
	db.session.commit()
	user_schema = User_schema()
	return user_schema.jsonify(user)


@user_routes.route('/covidData', methods=['GET'])
def get_data():
	response = [[]]
	response[0].append(['Fecha','Cantidad'])
	sourceDb ='https://datacovidcaldas.firebaseio.com/muestras.json'
	m=requests.get(sourceDb).json()
	for dato in m.values():
		response[0].append([dato['fecha'],dato['cantidad']])
	return jsonify(response)

@user_routes.route('/gptj', methods=['POST'])
def api_gptj():
	request_body = request.json
	translator = Translator()
	input_data = translator.translate(request_body['texto'], dest='en').text
	payload = {
        "context": input_data,
        "token_max_length": 100,
        "temperature": 0.8,
        "top_p": 0.9,
    }
	response = requests.post("http://api.vicgalle.net:5000/generate", params=payload).json()
	output = translator.translate(response["text"], dest='es').text
	return jsonify({'text': output})




@user_routes.route('/gptjneox', methods=['POST'])
def api_gptjneox():
	headers = {
	"accept": "*/*",
	"accept-language": "en-US,en;q=0.9",
	"authorization": "Bearer 842a11464f81fc8be43ac76fb36426d2",
	"content-type": "application/json",
	"sec-fetch-dest": "empty",
	"sec-fetch-mode": "cors",
	"sec-fetch-site": "same-site",
	"sec-gpc": "1",
	"Referer": "https://textsynth.com/",
	"Referrer-Policy": "strict-origin-when-cross-origin"
	}

	url = "https://api.textsynth.com/v1/engines/gptj_6B/completions"

	request_body = request.json
	translator = Translator()
	input_t = translator.translate(request_body['texto'], dest='en').text

	payload = json.dumps(json.loads('{"prompt":"'+input_t+'","temperature":1,"top_k":40,"top_p":0.9,"max_tokens":200,"stream":true,"stop":null}'))

	r = requests.post(url, headers=headers, data=payload)

	output = ""
	for l in r.text.split("\n"):
		if(l != ""):
			output += json.loads(l)['text'].replace("\n", "")
	output = translator.translate(output, dest='es').text

	return jsonify({'text': output})

@user_routes.route('/translateES', methods=['POST'])
def t_es():
	request_body = request.json
	translator = Translator()
	output = translator.translate(request_body['texto'], dest='es').text
	return jsonify({'text': output})

@user_routes.route('/translateEN', methods=['POST'])
def t_en():
	request_body = request.json
	translator = Translator()
	output = translator.translate(request_body['texto'], dest='en').text
	return jsonify({'text': output})