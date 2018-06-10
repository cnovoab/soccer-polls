from datetime import datetime
from . import db, ma, validate, Schema, fields


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    code = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return '<id {}>'.format(self.id)

class TeamSchema(ma.Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')
    id = fields.Integer(dump_only=True)
    name = fields.String(validate=not_blank)

    #self links
    def get_top_level_links(self, data, many):
      if many:
        self_link = "/teams/"
      else:
        self_link = "/teams/{}".format(data['id'])
      return {'self': self_link}

    class Meta:
        type_ = 'teams'
        # Fields to expose
        fields = ('name', 'code')

