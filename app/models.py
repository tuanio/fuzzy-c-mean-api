from app import db

class KhoaDaoTao(db.Model):
    __tablename__ = "khoadaotao"
    id = db.Column(db.Integer, primary_key=True)
    ten_kdt = db.Column(db.String(255))


class ChuyenNganh(db.Model):
    __tablename__ = "chuyennganh"
    id = db.Column(db.Integer, primary_key=True)
    ten_cn = db.Column(db.String(255))
    kdt_id = db.Column(db.Integer, db.ForeignKey("khoadaotao.id"))


class ChuongTrinhDaoTao(db.Model):
    __tablename__ = 'chuongtrinhdaotao'
    id = db.Column(db.Integer, primary_key=True)
    stt_monhoc = db.Column(db.Integer)
    ten_mh = db.Column(db.String(255))
    tin_chi = db.Column(db.Integer)
    kdt_id = db.Column(db.Integer, db.ForeignKey("khoadaotao.id"))
    

class SinhVien(db.Model):
    __tablename__ = 'sinhvien'
    id = db.Column(db.Integer, primary_key=True)
    ho_dem_sv = db.Column(db.String(255))
    ten_sv = db.Column(db.String(255))
    cn_id = db.Column(db.Integer, db.ForeignKey("chuyennganh.id"))
    kdt_id = db.Column(db.Integer, db.ForeignKey("khoadaotao.id"))


class DiemSinhVien(db.Model):
    __tablename__ = 'diemsinhvien'
    id = db.Column(db.Integer, primary_key=True)
    sv_id = db.Column(db.Integer, db.ForeignKey('sinhvien.id'))
    mh_id = db.Column(db.Integer, db.ForeignKey('chuongtrinhdaotao.id'))
    diem = db.Column(db.Float)


class ChiTietMonHocTheoChuyenNganh(db.Model):
    __tablename__ = 'chitietmonhoctheochuyennganh'
    id = db.Column(db.Integer, primary_key=True)
    stt_monhoc = db.Column(db.Integer)
    diem_tb = db.Column(db.Float) # diem trung binh cong


class DiemTuVan(db.Model):
    __tablename__ = 'diemtuvan'
    id = db.Column(db.Integer, primary_key=True)
    ten_sv = db.Column(db.String(255))
    ma_sv = db.Column(db.Integer)
    mh_id = db.Column(db.Integer, db.ForeignKey('chuongtrinhdaotao.id'))
    kdt_id = db.Column(db.Integer, db.ForeignKey('khoadaotao.id'))
    # cn_id = db.Column(db.Integer, db.ForeignKey('chuyennganh.id'))
    diem = db.Column(db.Float) # lưu lịch sử điểm user đã nhập


class NguoiDung(db.Model):
    __tablename__ = 'nguoidung'
    id = db.Column(db.Integer, primary_key=True)
    ten_nd = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))