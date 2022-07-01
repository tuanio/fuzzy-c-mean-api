from app import app
from app.utils import make_response, map_table, make_data
from flask_cors import cross_origin
from flask import request
import numpy as np


@app.route('/api/db/get-one/<path:table_name>/<int:id>', methods=['GET'])
@cross_origin()
def get_one(table_name: str, id: int):
    try:
        table = map_table[table_name]
        data = table.query.filter_by(id=id).first()
        data = vars(data)
    except Exception as e:
        return make_response(
            make_data(dict(error=str(e)), msg="Fail!", status="FAILURE")
        )
    
    return make_response(make_data(data=data, msg="Successfully!"))

@app.route('/api/db/get-all/<path:table_name>', methods=['GET'])
@cross_origin()
def get_all(table_name: str):
    try:
        table = map_table[table_name]
        data = table.query.all()
        data = list(map(vars, data))
    except Exception as e:
        return make_response(
            make_data(dict(error=str(e)), msg="Fail!", status="FAILURE")
        )
    
    return make_response(make_data(data=data, msg="Successfully!"))

@app.route('/api/db/update/<path:table_name>', methods=['PUT'])
@cross_origin()
def update(table_name: str):
    try:
        update_data = request.get_json(force=True)
        table = map_table[table_name]

        data = table.query.filter_by(id=update_data.get('id'))
        
        del update_data['id']
        data.update(update_data)
        
        db.session.commit()
    except Exception as e:
        return make_response(
            make_data(dict(error=str(e)), msg="Fail!", status="FAILURE")
        )
    
    return make_response(make_data(data=update_data, msg="Successfully!"))

@app.route('/api/db/add/<path:table_name>', methods=['POST'])
@cross_origin()
def add(table_name: str):
    try:
        new_data = request.get_json(force=True)
        table = map_table[table_name]
        
        data = table(**new_data)
        db.session.add(data)
        db.session.commit()

    except Exception as e:
        return make_response(
            make_data(dict(error=str(e)), msg="Fail!", status="FAILURE")
        )
    
    return make_response(make_data(data=new_data, msg="Successfully!"))

@app.route('/api/db/delete/<path:table_name>/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(table_name: str, id: int):
    try:
        table = map_table[table_name]
        data = table.query.filter_by(id=id).first()
        db.session.delete(data)
        db.session.commit()

    except Exception as e:
        return make_response(
            make_data(dict(error=str(e)), msg="Fail!", status="FAILURE")
        )
    
    return make_response(make_data(data=new_data, msg="Successfully!"))

