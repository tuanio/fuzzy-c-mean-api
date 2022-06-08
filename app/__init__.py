from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.routes import *
from app.utils import *