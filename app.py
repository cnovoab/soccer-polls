import os
from flask import Flask, render_template, request, jsonify
from models.shared import db

app = Flask(__name__)
db.init_app(app)

app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']


