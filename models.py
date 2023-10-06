from flask_sqlalchemy import SQLAlchemy
import uuid
import json

db = SQLAlchemy()

class Match(db.Model):
    matchId = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), nullable=False)
    playerId = db.Column(db.String(1), default="X", nullable=False)
    Xmoves = db.Column(db.JSON, nullable=False, default=json.dumps([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    Omoves= db.Column(db.JSON, nullable=False, default=json.dumps([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    status = db.Column(db.String(10), default="playing", nullable=False)

class User(db.Model):
    userId = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()), nullable=False)
    userName = db.Column(db.String(50), default="X", nullable=False)
    password = db.Column(db.String(50), default="X", nullable=False)