from . import Blueprint, request, jsonify, make_response, Api, Resource, SQLAlchemyError, ValidationError
from app.models import db, Team, TeamSchema

teams = Blueprint('teams', __name__)
schema = TeamSchema()
api = Api(teams)

class TeamsList(Resource):
    def get(self):
        query = Team.query.all()
        results = schema.dump(query, many=True).data
        return results

api.add_resource(TeamsList, '.json')
