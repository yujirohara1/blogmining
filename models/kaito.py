from api.database import db, ma

## 実テーブル
class Kaito(db.Model): 
    __tablename__ = "kaito"
    vendor_nm = db.Column(db.String(), primary_key=True) 
    system_nm = db.Column(db.String(), primary_key=True) 
    dantai_nm = db.Column(db.String(), primary_key=False) 
    tokosha_nm = db.Column(db.String(), primary_key=False) 
    situmon_kb = db.Column(db.Integer, primary_key=True) 
    hyoka_shubetu = db.Column(db.Integer, primary_key=True) 
    hyoka_shubetu_sub = db.Column(db.Integer, primary_key=False) 
    hyoka_value = db.Column(db.String(), primary_key=False) 
    hyoka_comment = db.Column(db.String(), primary_key=False) 
    ymdt = db.Column(db.DATETIME, nullable=False,primary_key=True)

class KaitoSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = Kaito
            load_instance = True


class VTokoGroupbyVendor(db.Model): 
    __tablename__ = "v_toko_groupby_vendor"
    vendor_nm = db.Column(db.String(), primary_key=True) 
    kensu = db.Column(db.Integer, primary_key=True) 
    rank1_avg = db.Column(db.Float , primary_key=True) 

class VTokoGroupbyVendorSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = VTokoGroupbyVendor
            load_instance = True

class VTokoGroupbySystem(db.Model): 
    __tablename__ = "v_toko_groupby_system"
    system_nm = db.Column(db.String(), primary_key=True) 
    kensu = db.Column(db.Integer, primary_key=True) 
    rank1_avg = db.Column(db.Float , primary_key=True) 

class VTokoGroupbySystemSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = VTokoGroupbySystem
            load_instance = True


#v_tokoradar_groupby_vendor
class VTokoRadarGroupByVendor(db.Model): 
    __tablename__ = "v_tokoradar_groupby_vendor"
    vendor_nm = db.Column(db.String(), primary_key=True) 
    shubetu1_avg = db.Column(db.Float , primary_key=True) 
    shubetu2_avg = db.Column(db.Float , primary_key=True) 
    shubetu3_avg = db.Column(db.Float , primary_key=True) 
    shubetu4_avg = db.Column(db.Float , primary_key=True) 
    shubetu5_avg = db.Column(db.Float , primary_key=True) 
    shubetu6_avg = db.Column(db.Float , primary_key=True) 
    shubetu7_avg = db.Column(db.Float , primary_key=True) 

class VTokoRadarGroupByVendorSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = VTokoRadarGroupByVendor
            load_instance = True


class VBunyaMapGroupbyVendor(db.Model): 
    __tablename__ = "v_bunyamap_groupby_vendor"
    vendor_nm = db.Column(db.String(), primary_key=True) 
    bunya_cd = db.Column(db.Integer, primary_key=True) 
    bunya_nm = db.Column(db.String(), primary_key=True) 
    ryaku_nm = db.Column(db.String(), primary_key=True) 
    kensu = db.Column(db.Integer, primary_key=True) 

class VBunyaMapGroupbyVendorSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = VBunyaMapGroupbyVendor
            load_instance = True


class VTodohukenGroupbyVendor(db.Model): 
    __tablename__ = "v_todohuken_groupby_vendor"
    vendor_nm = db.Column(db.String(), primary_key=True) 
    hyoka_value = db.Column(db.String(), primary_key=True) 
    kensu = db.Column(db.Integer, primary_key=True) 

class VTodohukenGroupbyVendorSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = VTodohukenGroupbyVendor
            load_instance = True
