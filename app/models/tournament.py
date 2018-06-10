from datetime import datetime
from . import db, ma, validate, Schema, fields


class Tournament(db.Model):
    __tablename__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    code = db.Column(db.String())
    start_datetime = db.Column(db.DateTime, nullable=True)
    finish_datetime = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self, name, code, start_datetime = None, finish_datetime = None):
        self.name = name
        self.code = code
        self.start_datetime = datetime.strptime(start_datetime, "%d%m%Y").date()
        self.finish_datetime = datetime.strptime(finish_datetime, "%d%m%Y").date()

class TournamentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'code', 'start_datetime', 'finish_datetime')
