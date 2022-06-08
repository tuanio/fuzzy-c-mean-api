from flask import Flask, request, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.routes import *
from app.utils import *