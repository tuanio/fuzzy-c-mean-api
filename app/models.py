from app import db

class KhoaDaoTao(db.Model):
    __tablename__ = "khoadaotao"
    kdt_id = db.Column(db.Integer, primary_key=True)
    ten_kdt = db.Column(db.String(255))


class ChuyenNganh(db.Model):
    __tablename__ = "chuyennganh"
    cn_id = db.Column(db.Integer, primary_key=True)
    ten_cn = db.Column(db.String(255))
    kdt_id = db.Column(db.String(255), db.ForeignKey("khoadaotao.kdt_id"))


class ChuongTrinhDaoTao(db.Model):
    __tablename__ = 'chuongtrinhdaotao'
    mh_id = db.Column(db.Integer, primary_key=True)
    stt_monhoc = db.Column(db.Integer)
    ten_mh = db.Column(db.String(255))
    tin_chi = db.Column(db.Integer)
    kdt_id = db.Column(db.Integer, db.ForeignKey("khoadaotao.kdt_id"))
    

class SinhVien(db.Model):
    __tablename__ = 'sinhvien'
    sv_id = db.Column(db.Integer, primary_key=True)
    ho_dem_sv = db.Column(db.String(255))
    ten_sv = db.Column(db.String(255))
    cn_id = db.Column(db.Integer, db.ForeignKey("chuyennganh.cn_id"))
    kdt_id = db.Column(db.Integer, db.ForeignKey("khoadaotao.kdt_id"))


class DiemSinhVien(db.Model):
    __tablename__ = 'diemsinhvien'
    diem_id = db.Column(db.Integer, primary_key=True)
    sv_id = db.Column(db.Integer, db.ForeignKey('sinhvien.sv_id'))
    mh_id = db.Column(db.Integer, db.ForeignKey('chuongtrinhdaotao.mh_id'))
    diem = db.Column(db.Float)


class ChiTietMonHocTheoChuyenNganh(db.Model):
    __tablename__ = 'chitietmonhoctheochuyennganh'
    ctmh_id = db.Column(db.Integer, primary_key=True)
    stt_monhoc = db.Column(db.Integer)
    diem = db.Column(db.Float)


class DiemTuVan(db.Model):
    __tablename__ = 'diemtuvan'
    dtv_id = db.Column(db.Integer, primary_key=True)
    sv_id = db.Column(db.Integer, db.ForeignKey('sinhvien.sv_id'))
    mh_id = db.Column(db.Integer, db.ForeignKey('chuongtrinhdaotao.mh_id'))
    kdt_id = db.Column(db.Integer, db.ForeignKey('khoadaotao.kdt_id'))
    cn_id = db.Column(db.Integer, db.ForeignKey('chuyennganh.cn_id'))
    diem = db.Column(db.Float) # lưu lịch sử điểm user đã nhập


class NguoiDung(db.Model):
    __tablename__ = 'nguoidung'
    nd_id = db.Column(db.Integer, primary_key=True)
    ten_nd = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))