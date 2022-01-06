#https://stackabuse.com/serving-static-files-with-flask
#https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html
#https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
#python3 -m http.server 5500 --bind 192.168.1.104

#source venv/bin/activate
#pip3 freeze > requirements.txt

#https://www.youtube.com/watch?v=-1DmVCPB6H8
#https://dev.to/techparida/how-to-deploy-a-flask-app-on-heroku-heb
#https://www.youtube.com/watch?v=BP3D03CYFHA

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# <string:user>
@app.route('/proto/<int:user>', methods=['GET'])
def proto(user):
	print(user)
	return jsonify({
        "nombre" :"sddf"
        })

@app.route('/enviar', methods=['POST'])
def enviar():
	msg = request.json
	print(msg)
	return "Recibido"

if __name__ == '__main__':
	app.run(debug=True, host="localhost", port=7000)



