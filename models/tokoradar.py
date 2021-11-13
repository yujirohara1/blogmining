from api.database import db, ma

## 実テーブル
class TokoRadar(db.Model): 
    __tablename__ = "toko_radar"
    vendor_nm = db.Column(db.String(), primary_key=True) 
    system_nm = db.Column(db.String(), primary_key=True) 
    dantai_nm = db.Column(db.String(), primary_key=False) 
    tokosha_nm = db.Column(db.String(), primary_key=False) 
    hyoka_shubetu = db.Column(db.Integer, primary_key=True) 
    hyoka_value = db.Column(db.Integer, primary_key=True) 
    ymdt = db.Column(db.DATETIME, nullable=False,primary_key=True)

class TokoRadarSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = TokoRadar
            load_instance = True

