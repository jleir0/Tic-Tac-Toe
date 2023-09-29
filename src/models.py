from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Match(db.Model):
    matchId = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), unique=True, nullable=False)
    