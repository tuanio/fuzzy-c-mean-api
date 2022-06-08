from app import app
from app.utils import make_response, get_model
from flask_cors import cross_origin
from flask import request
import numpy as np

@app.route('/')
@cross_origin()
def index():
    return make_response(dict(data="Home"))

@app.route('/get-recommend', methods=['GET', 'POST'])
@cross_origin()
def get_recommend():
    scores_dict = request.get_json(force=True)
    scores_dict = {k: float(v) for k, v in scores_dict.items()}

    mmt = get_model('mmt', scores_dict)
    cnpm = get_model('cnpm', scores_dict)
    khptdl = get_model('khptdl', scores_dict)
    httt = get_model('httt', scores_dict)
    
    ret = {
        "mmt": mmt,
        "cnpm": cnpm,
        "khptdl": khptdl,
        "httt": httt
    }

    return make_response(ret)