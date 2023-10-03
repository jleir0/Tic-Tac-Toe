from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class Match(db.Model):
    matchId = db.Column(db.String(36), default=str(uuid.uuid4()), nullable=False)
    playerId = db.Column(db.String(1), default="X", nullable=False)
    Xmoves = db.Column(db.JSON, nullable=False, default=db.json.dumps([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    Omoves= db.Column(db.JSON, nullable=False, default=db.json.dumps([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    status = db.Column(db.String(10), default="playing", nullable=False)
