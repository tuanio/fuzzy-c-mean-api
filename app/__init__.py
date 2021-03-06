from flask import Flask, request, jsonify
import os
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}}) # change from '*' to this route 
# CORS(app, resources={
#     r"*": {
#         "origins": [
#             "https://fuzzy-c-mean-fe.vercel.app",
#             "http://localhost:5502"
#         ]}
#     }) # change from '*' to this route 
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# username = os.environ["PGUSER"]
# password = os.environ["PGPASSWORD"]
# db_name = os.environ["PGDATABASE"]
# host = os.environ["PGHOST"]
# port = os.environ["PGPORT"]
# uri = os.environ["DATABASE_URL"]

# local config database
# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = f"postgresql://{username}:{password}@{host}:{port}/{db_name}"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', None)

db = SQLAlchemy(app)

status_code = dict(SUCCESS=1, FAILURE=0)

from app.routes import *
from app.utils import *
