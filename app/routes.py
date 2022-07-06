from app import app
from app.utils import (
    make_response,
    get_model_fuzzy_c_mean,
    map_subjects,
    get_distance,
    list_majors,
    get_data
)
from app.models import *
from flask_cors import cross_origin
from flask import request
import numpy as np

from .db_routes import *

@app.route('/')
@cross_origin()
def index():
    return make_response(dict(data="Home"))

@app.route('/api/get-recommend-fuzzy-c-mean', methods=['GET', 'POST'])
@cross_origin()
def get_recommend_fuzzy_c_mean():
    scores_dict = request.get_json(force=True)
    scores_dict = {k: float(v) for k, v in scores_dict.items()}

    mmt = get_model_fuzzy_c_mean('mmt', scores_dict)
    cnpm = get_model_fuzzy_c_mean('cnpm', scores_dict)
    khptdl = get_model_fuzzy_c_mean('khptdl', scores_dict)
    httt = get_model_fuzzy_c_mean('httt', scores_dict)
    
    ret = {
        "mmt": mmt,
        "cnpm": cnpm,
        "khptdl": khptdl,
        "httt": httt
    }

    return make_response(ret)

@app.route('/api/get-recommend', methods=['POST'])
@cross_origin()
def get_recommend():
    data = request.get_json(force=True)

    data['scores_dict'] = {k: float(v) for k, v in data['scores_dict'].items()}

    kdt = KhoaDaoTao.query.filter_by(ten_kdt=data['khoa_hoc']).first()

    for subj_abbr, score in data['scores_dict'].items():
        subj_name = map_subjects[subj_abbr]
        mh = ChuongTrinhDaoTao.query.filter_by(
            ten_mh=subj_name,
            kdt_id=kdt.id
        ).first()
        dtv = DiemTuVan(
            ma_sv=int(data['ma_sv']),
            ten_sv=data['ten_sv'],
            mh_id=mh.id,
            kdt_id=kdt.id,
            diem=score
        )
        db.session.add(dtv)
    db.session.commit()

    distances = np.array([
        get_distance(major, data['scores_dict'], kdt.id)
        for major in list_majors
    ])

    distances = (100 - (distances / distances.sum() * 100).round(2)).tolist()

    ret = dict(zip(list_majors, distances))

    return make_response(ret)

@app.route('/api/authorize/<path:username>/<path:password>', methods=['GET'])
@cross_origin()
def authorize(username: str, password: str):
    user = NguoiDung.query.first()
    flag = False
    if user.username == username and user.password == password:
        flag = True
    
    return make_response(dict(is_okay=flag))