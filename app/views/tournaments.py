from . import Blueprint, request, jsonify, make_response, Api, Resource, SQLAlchemyError, ValidationError
from app.models import db, Tournament, TournamentSchema

tournaments = Blueprint('tournaments', __name__)
schema = TournamentSchema()
api = Api(tournaments)

class TournamentsList(Resource):
    def get(self):
        tournaments_query = Tournament.query.all()
        results = schema.dump(tournaments_query, many=True).data
        return results

api.add_resource(TournamentsList, '.json')
