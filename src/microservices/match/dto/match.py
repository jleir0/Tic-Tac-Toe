from flask_restx import fields

match_model = {
    'matchId': fields.String(description='The matchs ID'),
    'playerId': fields.String(description='The acting player. X or O.'),
    'square': fields.Nested({
        'x': fields.Integer(description='X-coordinate of the target square'),
        'y': fields.Integer(description='Y-coordinate of the target square')
    }, description='The target square to mark')
}
