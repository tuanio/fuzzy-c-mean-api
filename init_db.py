import os
import glob
from dataring.transform_data import transform

from app import db

db.drop_all()
db.create_all()

filepaths = glob.glob('data/*')

with open('transform_data_log.txt', 'w') as f:
    f.write('')

for filepath in filepaths:
    transform(filepath)
    print(f"Done file {filepath}")