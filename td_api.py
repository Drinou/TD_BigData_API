from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

Drinou = Flask(__name__)

Drinou.config['MONGO_DBNAME'] = 'restdb'
Drinou.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

# Lancer MongoDB : entrer dans le terminal $ sudo docker run -it -p 27017:27017 mongo
# Et dans MongoDB : entrer l'URI mongodb://localhost:27017/restdb

mongo = PyMongo(Drinou)

# Quand le client se connecte au serveur
@Drinou.route("/")
def setup():
    return "Bonjour et bienvenue sur l'API de Drinou"

# Requête URL, methode GET (copie toutes les données dans la database users, soit la collection user : name et distance, ...)
@Drinou.route('/user', methods=['GET'])
def get_all_user():
    return "Coucou toi ! Tu es bien dans le user ;)"

# Requête URL, methode GET (copie une donnée dans la collection : name ou distance ou ...)
@Drinou.route('/user/one', methods=['GET'])
def get_one_user():
    return "Héhé petit.e coquin.e tu es le number one !"

# L'application se lance
if __name__ == '__main__':
    Drinou.run(debug=True, host = "0.0.0.0")

#Grimoire de Formules Magiques :
#create images docker : sudo docker build -t princessedrinou/td_bigdata_api .
#se connecter à son compte dockerhub (hub.docker.com) sudo docker login -u princessedrinou
#envoyer l'image dans la stratosphère (Terminal VS Code -> hub.docker.com) sudo docker push princessedrinou/td_bigdata_api
