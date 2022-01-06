from flask import Blueprint, jsonify, request

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
	user_schema = User_schema()
	return user_schema.jsonify(user)

@user_routes.route('/api/user/<int:id>', methods=['PUT'])
def update_user(id):
	user = User.query.get(id)
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
	db.session.delete(user)
	db.session.commit()
	user_schema = User_schema()
	return user_schema.jsonify(user)
