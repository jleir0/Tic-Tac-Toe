"""Organization Services."""

from uuid import UUID, uuid4
from flask_restx import marshal


class MatchServices(object):
    """Organization Service API."""

    @staticmethod
    def place_mark(args):
        return 200, "Okey"
    
    @staticmethod
    def get_match(matchId):
        return 200, "Okey"
    
    @staticmethod
    def post_match():
        return 200, "Okey"
