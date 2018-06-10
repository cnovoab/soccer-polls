from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_jsonapi import Schema, fields
from marshmallow import validate

db = SQLAlchemy()
ma = Marshmallow()
from team import Team, TeamSchema
from tournament import Tournament, TournamentSchema
