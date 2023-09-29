from flask_restx import Namespace, Resource
from flask import request, abort
from models import db, Match
import uuid

match_api = Namespace('match', description='Operaciones de Juego')

@match_api.route('/move')
class MatchResource(Resource):
    def post(self):
        """Each player will use it to play a move within the game."""
        return 200
    
@match_api.route('/status/<string:matchId>')
class MatchResource(Resource):
    def get(self, matchId):
        try:
            match = Match.query.filter_by(matchId=matchId).first()

            if match is None:
                abort(404, f"Match with id {matchId} not found")

            response_data = {
                "matchId": match.matchId
            }

            return response_data, 200
        except Exception as e:
            db.session.rollback()
            abort(500, f"An error occurred: {str(e)}")

@match_api.route('/create')
class MatchResource(Resource):
    def post(self):
        """
        This endpoint will be used to request the creation of a new match.
        It will provide the new match’s matchId.
        """
        try:
            matchId = str(uuid.uuid4())

            response_data = {
                "matchId": matchId
            }

            new_match = Match(matchId=matchId)
            db.session.add(new_match)
            db.session.commit()

            return response_data, 200
        except Exception as e:
            db.session.rollback()
            abort(500, f"An error occurred: {str(e)}")
