from flask import jsonify
import pickle
import numpy as np

def make_response(data={}, status=200):
    '''
        - Make a resionable response with header
        - status default is 200 mean ok
    '''
    res = jsonify(data)
    res.headers.add('Access-Control-Allow-Origin', '*')
    res.headers.add('Content-Type', 'application/json')
    res.headers.add('Accept', 'application/json')
    return res

def get_model(major, scores_dict):
    assert major in ['mmt', 'cnpm', 'khptdl', 'httt'], "Major not found."
    
    if major == 'khptdl':
        subj = ['nhập môn lập trình', 'toán rời rạc', 'khai thác dữ liệu', 'cơ sở dữ liệu']
    elif major == 'httt':
        subj = ['cơ sở dữ liệu', 'hệ quản trị cơ sở dữ liệu', 'nhập môn lập trình', 'cấu trúc dữ liệu và giải thuật']
    elif major == 'cnpm':
        subj = ['nhập môn lập trình', 'lập trình hướng đối tượng', 'cơ sở dữ liệu']
    else:
        subj = ['kiến trúc máy tính', 'mạng máy tính', 'nhập môn lập trình', 'hệ điều hành']
    
    scores = np.array([[np.nan if isinstance(scores_dict[i], str) else scores_dict[i] for i in subj]])
    print(scores)

    with open(f'models/{major}.model', 'rb') as f:
        model = pickle.load(f)
        print(f"Load model {major} successfully!")

    probability = model.soft_predict(scores).reshape(-1)[1] * 100
    return round(probability, 2)