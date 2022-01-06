from utils.db import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(80), nullable=False)
	apellido = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)

	def __init__(self, nombre, apellido, email):
		self.nombre = nombre
		self.apellido = apellido
		self.email = email