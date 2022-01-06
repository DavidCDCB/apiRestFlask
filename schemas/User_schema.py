from flask_marshmallow import Marshmallow

ma = Marshmallow()

class User_schema(ma.Schema):
	class Meta:
		fields = ('id', 'nombre', 'apellido', 'email')

