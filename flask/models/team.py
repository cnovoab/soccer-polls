from app import db
import datetime
from sqlalchemy import DateTime

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    code = db.Column(db.String())
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.id)

