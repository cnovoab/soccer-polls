from flask import Flask, Response
from app.models import *

class MyResponse(Response):
     default_mimetype = 'application/xml'

# http://flask.pocoo.org/docs/1.0/patterns/appfactories/
def create_app():
    import os
    from flask import Flask, render_template, request, jsonify

    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.response_class = MyResponse
    db.init_app(app)

    # Blueprints
    from app.views.tournaments import tournaments
    from app.views.teams import teams
    app.register_blueprint(tournaments, url_prefix='/api/v1/tournaments')
    app.register_blueprint(teams, url_prefix='/api/v1/teams')

    return app
