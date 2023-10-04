from flask import Flask
from flask_restx import Api
from models import db
from microservices.match.controllers.match import match_api
from config import DB_URI, Session, engine

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app, version='1.0', title='API de Juegos', description='API para gestionar juegos')
api.add_namespace(match_api)

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
        
    app.run(host='0.0.0.0', port=5000)

