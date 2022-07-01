import os
import glob
from dataring.transform_data import transform

from app import db
from app.models import *
from sqlalchemy import func

db.drop_all()
db.create_all()

filepaths = glob.glob('data/*')

with open('transform_data_log.txt', 'w') as f:
    f.write('')

for filepath in filepaths:
    transform(filepath)
    print(f"Done file {filepath}")

data = (
    db.session.query(
        ChuongTrinhDaoTao.stt_monhoc,
        func.avg(DiemSinhVien.diem).label('diem_tb')
    ).filter(
        ChuongTrinhDaoTao.stt_monhoc != 0,
        DiemSinhVien.diem != 0
    ).join(DiemSinhVien,
        DiemSinhVien.mh_id == ChuongTrinhDaoTao.id
    ).group_by(ChuongTrinhDaoTao.stt_monhoc)
    .all()
)

for stt_monhoc, diem_tb in data:
    datum = ChiTietMonHocTheoChuyenNganh(stt_monhoc=stt_monhoc, diem_tb=diem_tb)
    db.session.add(datum)
db.session.commit()