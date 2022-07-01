from flask import jsonify
import pickle
import numpy as np
from .models import *
from app import status_code

list_majors = ['mmt', 'cnpm', 'khptdl', 'httt']

list_table_names = [
    'khoadaotao',
    'chuyennganh',
    'chuongtrinhdaotao',
    'sinhvien',
    'diemsinhvien',
    'chitietmonhoctheochuyennganh',
    'diemtuvan',
    'nguoidung'
]

list_table_objects = [
    KhoaDaoTao,
    ChuyenNganh,
    ChuongTrinhDaoTao,
    SinhVien,
    DiemSinhVien,
    ChiTietMonHocTheoChuyenNganh,
    DiemTuVan,
    NguoiDung
]

map_table = dict(zip(list_table_names, list_table_objects))

list_subjects_abbr = [
    'nmlt',
    'trr',
    'ktdl',
    'csdl',
    'hqtcsdl',
    'ctdlgt',
    'lthdt',
    'ktmt',
    'mmt',
    'hdh'
]

list_subjects = [
    'nhập môn lập trình',
    'toán rời rạc',
    'khai thác dữ liệu',
    'cơ sở dữ liệu',
    'hệ quản trị cơ sở dữ liệu',
    'cấu trúc dữ liệu và giải thuật',
    'lập trình hướng đối tượng',
    'kiến trúc máy tính',
    'mạng máy tính',
    'hệ điều hành'
]

map_subjects = dict(zip(list_subjects_abbr, list_subjects))

def make_response(data={}, status=200):
    '''
        - Make a resionable response with header
        - status default is 200 mean ok
    '''
    res = jsonify(data)
    # res.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5502')
    res.headers.add('Content-Type', 'application/json')
    res.headers.add('Accept', 'application/json')
    return res

def get_model_fuzzy_c_mean(major, scores_dict):
    '''
        get fuzzy c mean model for prediction
    '''
    assert major in ['mmt', 'cnpm', 'khptdl', 'httt'], "Major not found."
    
    if major == 'khptdl':
        subj = ['nmlt', 'trr', 'ktdl', 'csdl']
    elif major == 'httt':
        subj = ['csdl', 'hqtcsdl', 'nmlt', 'ctdlgt']
    elif major == 'cnpm':
        subj = ['nmlt', 'lthdt', 'csdl']
    else:
        subj = ['ktmt', 'mmt', 'nmlt', 'hdh']
    
    scores = np.array([[np.nan if isinstance(scores_dict[i], str) else scores_dict[i] for i in subj]])

    with open(f'models/{major}.model', 'rb') as f:
        model = pickle.load(f)
        print(f"Load model {major} successfully!")

    probability = model.soft_predict(scores).reshape(-1)[1] * 100
    return round(probability, 2)

def get_distance(major, scores_dict, kdt_id):
    assert major in ['mmt', 'cnpm', 'khptdl', 'httt'], "Major not found."
    
    if major == 'khptdl':
        subj = ['nmlt', 'trr', 'ktdl', 'csdl']
    elif major == 'httt':
        subj = ['csdl', 'hqtcsdl', 'nmlt', 'ctdlgt']
    elif major == 'cnpm':
        subj = ['nmlt', 'lthdt', 'csdl']
    else:
        subj = ['ktmt', 'mmt', 'nmlt', 'hdh']
    
    user_scores = np.array([[np.nan if isinstance(scores_dict[i], str) else scores_dict[i] for i in subj]])
    
    subj_names = [map_subjects[i] for i in subj]
    list_stt_mon_hoc = [
        ChuongTrinhDaoTao.query.filter_by(
            ten_mh=ten,
            kdt_id=kdt_id
        ).first().stt_monhoc
        for ten in subj_names
    ]

    comp_scores = np.array([[
        ChiTietMonHocTheoChuyenNganh.query.filter_by(
            stt_monhoc=i
        ).first().diem_tb for i in list_stt_mon_hoc
    ]])

    distance = np.linalg.norm(user_scores - comp_scores)
    return distance

def make_data(data: dict = dict(), msg: str = "", status: str = "SUCCESS") -> dict:
    ret_data = dict(data=data, msg=msg, status_code=status_code[status])
    return ret_data
