from app import app
from app.utils import make_response, get_model
from flask import request
import numpy as np

@app.route('/')
def index():
    return make_response(dict(data="Home"))

@app.route('/get-recommend', methods=['GET', 'POST'])
def get_recommend():
    scores_dict = request.get_json(force=True)

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