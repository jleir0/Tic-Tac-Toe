from flask_restx import Namespace, Resource
from flask import  abort
from src.microservices.match.dto.match import match_model
from sqlalchemy import desc
import uuid
from ..services.match import MatchService

match_api = Namespace('match', description='Operaciones de Juego')

@match_api.route('/move')
class MoveMatch(Resource):
    @match_api.expect(match_model)
    def post(self):
        """
        This endpoint allow to maka a move in a match.
        """
        try:
            data = match_api.payload
            return MatchService.move(data)
        except Exception as e:
            abort(500, f"An error occurred: {str(e)}")

@match_api.route('/status/<string:matchId>')
class StatusMatch(Resource):
    def get(self, matchId):
        """
        This endpoint retrieve status of a match.
        """
        try:
            return MatchService.status(matchId)
        except Exception as e:
            abort(500, f"An error occurred: {str(e)}")
        
@match_api.route('/create')
class CreateMatch(Resource):
    def post(self):
        """
        This endpoint will be used to request the creation of a new match.
        It will provide the new match’s matchId.
        """
        try:
            matchId = str(uuid.uuid4())
            return MatchService.create(matchId)
        except Exception as e:
            abort(500, f"An error occurred: {str(e)}")
