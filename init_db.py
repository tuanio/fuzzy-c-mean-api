import os

os.system('python transform_data.py')

from app import db

db.drop_all()
db.create_all()
