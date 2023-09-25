"""Match controller."""
from flask_restx import Resource, reqparse
from flask_restful import Api, abort
from ..dto.match import MatchDTO
from ..service.match import MatchServices

api = MatchDTO.api

@api.rout("/move")
class MarkMovementApi(Resource):
    """Mark Movement Api."""

    @api.doc(description="Play a move within the game.")
    @api.response(200, "Mark placed.", MatchDTO.placeMark)
    @api.response(400, "Bad request.")
    @api.response(404, "Not found.")
    def post(self):
        """Play a move within the game."""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "matchId",
                type=int,
                required=True,
                help="The match´s ID."
            )
            parser.add_argument(
                "playerId",
                type=str,
                required=True,
                default="X",
                help="The mark to be placed: X o O."
            )
            parser.add_argument(
                "square",
                type=dict,
                required=True,
                help="The target square to mark."
            )
            args = parser.parse_args()
            return MatchServices.place_mark(args)
        except Exception as e:
            return {'message': 'Internal server error'}, 500

@api.rout("/status/<int:matchId>")
class MatchStatusApi(Resource):
    """Match Status Api."""

    @api.doc(description="Current status of a given match.")
    @api.response(200, "Current status.")
    @api.response(400, "Bad request.")
    @api.response(404, "Not found.")
    def get(self, matchId):
        """Play a move within the game."""
        try:
            return MatchServices.get_match(matchId)
        except Exception as e:
            return {'message': 'Internal server error'}, 500

@api.rout("/create")
class MatchCreatorApi(Resource):
    """Match Creator Api."""

    @api.doc(description="Create a new match.")
    @api.response(200, "Match created.", MatchDTO.newMatch)
    @api.response(400, "Bad request.")
    @api.response(404, "Not found.")
    def post(self):
        """Create a new match."""
        try:
            return MatchServices.post_match()
        except Exception as e:
            return {'message': 'Internal server error'}, 500