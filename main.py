#https://stackabuse.com/serving-static-files-with-flask
#https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html
#https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
#python3 -m http.server 5500 --bind 192.168.1.104

#source venv/bin/activate
#pip3 freeze > requirements.txt

#https://www.youtube.com/watch?v=-1DmVCPB6H8
#https://dev.to/techparida/how-to-deploy-a-flask-app-on-heroku-heb
#https://www.youtube.com/watch?v=BP3D03CYFHA

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from utils.db import db
from routes.User_routes import user_routes

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ull723k51nkuwjps:WJIl1nNcF0gvMvRAQbf5@b84ertg3lptxeayohgqa-mysql.services.clever-cloud.com/b84ertg3lptxeayohgqa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)
Marshmallow(app)

app.register_blueprint(user_routes)

with app.app_context():
	db.create_all()

if __name__ == '__main__':
	app.run(debug=True, host="localhost", port=7000)



