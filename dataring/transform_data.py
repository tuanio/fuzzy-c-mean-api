#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sys
from app import *
from app.models import *


# In[2]:

def transform(filepath):

    # In[3]:

    try:
        df = pd.read_excel(filepath)


        # In[4]:

        # In[5]:


        mon_tu_van = [
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

        # In[6]:


        # # KhoaDaoTao

        # In[7]:


        ten_kdt = df.iloc[3, 12].split(':')[-1].strip()

        kdt = KhoaDaoTao.query.filter_by(ten_kdt=ten_kdt).first()

        if kdt is None:

            kdt = KhoaDaoTao(ten_kdt=ten_kdt)
            db.session.add(kdt)
            db.session.commit()
            
        kdt_id = kdt.id

        # In[8]:

        # # ChuyenNganh

        # In[9]:


        ten_cn = df.iloc[5, 1].split(':')[-1].strip()
        ten_cn

        cn = ChuyenNganh(ten_cn=ten_cn, kdt_id=kdt_id)
        db.session.add(cn)
        db.session.commit()
        cn_id = cn.id

        # In[10]:

        # # ChuongTrinhDaoTao

        # In[11]:


        all_subjects = df.iloc[7, 5:-6].values
        all_subjects.shape


        # In[12]:


        tin_chi = list(map(lambda x: int(x.strip()), df.iloc[8, 5:-6].values))

        # In[13]:

        list_mh_id = []

        for subj, tc in zip(all_subjects, tin_chi):
            subj = subj.lower()
            idx = 0
            if subj in mon_tu_van:
                idx = mon_tu_van.index(subj) + 1

            datum = dict(
                stt_monhoc=idx,
                ten_mh=subj,
                tin_chi=tc,
                kdt_id=kdt_id
            )
            
            ctdt = ChuongTrinhDaoTao.query.filter_by(**datum).first()

            if ctdt is None:
                ctdt = ChuongTrinhDaoTao(**datum)

                db.session.add(ctdt)
                db.session.commit()

            list_mh_id.append(ctdt.id)

        # In[14]:

        # In[15]:

        # # SinhVien

        # In[16]:


        ho_dem, ten = df.iloc[9:-2, 2:4].values.T
        ho_dem = ho_dem.tolist()
        ten = ten.tolist()

        # In[17]:


        list_sv_id = []
        for hd, t in zip(ho_dem, ten):
            sv = SinhVien(
                ho_dem_sv=hd,
                ten_sv=t,
                cn_id=cn_id,
                kdt_id=kdt_id
            )
            db.session.add(sv)
            db.session.commit()

            list_sv_id.append(sv.id)


        # In[18]:


        # In[19]:

        # # DiemSinhVien

        # In[20]:


        diem = df.iloc[9:-2, 5:-6].fillna(0).astype('float').values.tolist()
        # In[21]:

        for i in range(len(diem)):
            for j in range(len(diem[i])):

                sv_id = list_sv_id[i]
                mh_id = list_mh_id[j]

                dsv = DiemSinhVien(sv_id=sv_id, mh_id=mh_id, diem=diem[i][j])
                db.session.add(dsv)
        
        db.session.commit()

        with open('transform_data_log.txt', 'a', encoding='utf-8') as f:
            f.write('\n' + '=' * 100 + '\n')
            f.write(f"Done {filepath}")

    except Exception as e:
        with open('transform_data_log.txt', 'a', encoding='utf-8') as f:
            f.write('\n' + '=' * 100 + '\n')
            f.write(str(e))