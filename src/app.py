# En app.py

from flask import Flask
from flask_restx import Api
from microservices.match import match_api

app = Flask(__name__)
api = Api(app, version='1.0', title='API de Juegos', description='API para gestionar juegos')
api.add_namespace(match_api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

