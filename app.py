from flask import Flask
from flask_restx import Api
from models import db
from src.microservices.match.controllers.match import match_api
from src.microservices.user.controllers.user import user_api
from config import DB_URI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app, version='1.0', title='API de Juegos', description='API para gestionar juegos')
api.add_namespace(match_api)
api.add_namespace(user_api)

db.init_app(app)

with app.app_context():
        db.create_all()

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)

