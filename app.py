from flask import Flask
from flask_restx import Api
from models import db
from src.microservices.match.controllers.match import match_api
from config import DB_URI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app, version='0.7.0', title='Tic-Tac-Toe', description='API para jugar Tic-Tac-Toe')
api.add_namespace(match_api)

db.init_app(app)

with app.app_context():
        db.create_all()

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)

