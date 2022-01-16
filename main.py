#https://stackabuse.com/serving-static-files-with-flask
#https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html
#https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
#python3 -m http.server 5500 --bind 192.168.1.104

#https://codigofacilito.com/articulos/deploy-flask-heroku

#sudo pip3 install virtualenv
#virtualenv venv
#source venv/bin/activate
#pip3 freeze > requirements.txt
#deactivate

#pip3 install flask flask_cors gunicorn flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy pymysql

#https://www.youtube.com/watch?v=-1DmVCPB6H8
#https://dev.to/techparida/how-to-deploy-a-flask-app-on-heroku-heb
#https://www.youtube.com/watch?v=BP3D03CYFHA

from flask import Flask
from flask_cors import CORS

from utils.db import db, database_config
from routes.User_routes import user_routes

app = Flask(__name__)
CORS(app)

database_config(app)

app.register_blueprint(user_routes)

with app.app_context():
	db.create_all()

if __name__ == '__main__':
	app.run(debug=True, host="localhost", port=7000)



