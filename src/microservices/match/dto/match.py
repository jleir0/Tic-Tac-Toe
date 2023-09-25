"""Match DTO."""
from flask_restx import Namespace, fields

class MatchDTO:
    """DTO Class."""

    api = Namespace("matches", description="Match API")

    placeMark = api.model(
        "placeMarkQuery",
        {
            "matchId": fields.String,
            "playerId": fields.String,
            "square": {
                "X": fields.String,
                "Y": fields.String,
            }
        }
    )

    newMatch = api.model(
        "newMatchResponse",
        {
            "matchId": fields.String,
        }
    )
