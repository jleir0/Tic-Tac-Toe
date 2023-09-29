from flask_restx import Namespace, Resource
from flask import request, jsonify

import uuid

match_api = Namespace('match', description='Operaciones de Juego')

@match_api.route('/move')
class MatchResource(Resource):
    def post(self):
        """Each player will use it to play a move within the game."""
        return 200
    
@match_api.route('/status')
class MatchResource(Resource):
    def get(self):
        """This endpoint returns the current status of a given match."""
        match_id = request.args.get('match_id') 
        return 200, match_id

@match_api.route('/create')
class MatchResource(Resource):
    def post(self):
        """
        This endpoint will be used to request the creation of a new match.
        It will provide the new match’s matchId.
        """
        matchId = str(uuid.uuid4())
        d_matchId = {
            "matchId": matchId
        }
        return jsonify(d_matchId), 200
