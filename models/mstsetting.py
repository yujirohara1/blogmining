from api.database import db, ma

class MstSetting(db.Model): 
    __tablename__ = "mst_setting" 
    param_id = db.Column(db.String(), primary_key=True) 
    param_nm = db.Column(db.String(), nullable=False) 
    param_no = db.Column(db.Integer, primary_key=True) 
    param_val1 = db.Column(db.String(), nullable=False) 
    param_val2 = db.Column(db.String(), nullable=False) 
    param_val3 = db.Column(db.String(), nullable=False) 
    tenant_id   = db.Column(db.String(), primary_key=True) 

class MstSettingSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = MstSetting
            load_instance = True

#      列     |         タイプ         | 照合順序 | Null 値を許容 | デフォルト
# ------------+------------------------+----------+---------------+------------
#  param_id   | character varying(30)  |          | not null      |
#  param_nm   | character varying(80)  |          | not null      |
#  param_no   | integer                |          | not null      |
#  param_val1 | character varying(200) |          | not null      |
#  param_val2 | character varying(200) |          |               |
#  param_val3 | character varying(200) |          |               |
# インデックス:
#     "mst_setting_pkey" PRIMARY KEY, btree (param_id, param_no)
# 