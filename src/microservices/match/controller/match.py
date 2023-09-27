"""Match controller."""
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from ..service.match import MatchServices
from microservices.match.dto.match import MatchDTO

match_api = Blueprint('match_api', __name__)
match_api.route('/')
def ruta_raiz():
    return "¡Hola, esta es la página de inicio de la aplicación match_api!"

