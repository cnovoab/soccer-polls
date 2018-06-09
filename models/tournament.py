from sqlalchemy import DateTime

class Team(db.Model):
    __tablename__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    code = db.Column(db.String())
    start_datetime = db.Column(DateTime, nullable=True)
    finish_datetime = db.Column(DateTime, nullable=True)
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.id)

