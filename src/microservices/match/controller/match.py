"""Match controller."""
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from ..service.match import MatchServices
from microservices.match.dto.match import MatchDTO

match_api = Blueprint('match_api', __name__)
api = Api(match_api)

class MoveResource(Resource):
    def post(self):
        match_parser = reqparse.RequestParser()
        match_parser.add_argument('matchId', type=str, required=True, help='The match´s ID.')
        match_parser.add_argument('playerId', type=str, required=True, help='The acting player. X or O.')
        match_parser.add_argument('square', type=str, required=True, help='The target square to mark.')        
        args = match_parser.parse_args(strict=True)
        return MatchServices.place_mark(args)
api.add_resource(MoveResource, '/move', endpoint='move')

class StatusResource(Resource):
    def get(self,matchId):
        return MatchServices.get_match(matchId)
api.add_resource(StatusResource, '/status/<string:matchId>', endpoint='status')

class CreateResource(Resource):
    def post(self):
        return MatchServices.post_match()
api.add_resource(CreateResource, '/create', endpoint='create')