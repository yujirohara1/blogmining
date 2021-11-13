from api.database import db, ma

## 実テーブル
class Daicho(db.Model): 
    __tablename__ = "daicho" 
    customer_id = db.Column(db.Integer, primary_key=True) 
    item_id = db.Column(db.Integer, primary_key=True) 
    youbi = db.Column(db.Integer, primary_key=True) 
    quantity = db.Column(db.Integer, nullable=False) 
    tenant_id   = db.Column(db.String(), primary_key=True) 
    

class DaichoSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = Daicho
            load_instance = True

## ビュー
class VDaichoA(db.Model): 
    __tablename__ = "v_daicho_a" 
    group_id     = db.Column(db.Integer, nullable=False) 
    list         = db.Column(db.Integer, nullable=True) 
    customer_id  = db.Column(db.Integer, primary_key=True) 
    tenpo        = db.Column(db.String,  nullable=True) 
    cname1       = db.Column(db.String,  nullable=True) 
    cname2       = db.Column(db.String,  nullable=True) 
    address1     = db.Column(db.String,  nullable=True) 
    address2     = db.Column(db.String,  nullable=True) 
    address3     = db.Column(db.String,  nullable=True) 
    harai_kb     = db.Column(db.Integer, nullable=True) 
    cdelflg      = db.Column(db.Integer, nullable=True) 
    item_id      = db.Column(db.Integer, primary_key=True) 
    icode        = db.Column(db.String, nullable=True) 
    iname1       = db.Column(db.String, nullable=True) 
    iname2       = db.Column(db.String, nullable=True) 
    tanka        = db.Column(db.Integer, nullable=True) 
    idelflg      = db.Column(db.Integer, nullable=True) 
    getu         = db.Column(db.Integer, nullable=True) 
    ka           = db.Column(db.Integer, nullable=True) 
    sui          = db.Column(db.Integer, nullable=True) 
    moku         = db.Column(db.Integer, nullable=True) 
    kin          = db.Column(db.Integer, nullable=True) 
    dou          = db.Column(db.Integer, nullable=True) 
    niti         = db.Column(db.Integer, nullable=True) 
    total        = db.Column(db.Integer, nullable=True) 
    tenant_id   = db.Column(db.String(), primary_key=True) 

class VDaichoASchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = VDaichoA
            load_instance = True


##     列      |         タイプ         | 照合順序 | Null 値を許容 | デフォルト
##-------------+------------------------+----------+---------------+------------
## group_id    | integer                |          |               |
## list        | integer                |          |               |
## customer_id | integer                |          |               |
## tenpo       | character varying(200) |          |               |
## cname1      | character varying(80)  |          |               |
## cname2      | character varying(80)  |          |               |
## address1    | character varying(80)  |          |               |
## address2    | character varying(80)  |          |               |
## address3    | character varying(80)  |          |               |
## harai_kb    | integer                |          |               |
## cdelflg     | integer                |          |               |
## item_id     | integer                |          |               |
## icode       | character varying(20)  |          |               |
## iname1      | character varying(80)  |          |               |
## iname2      | character varying(80)  |          |               |
## tanka       | integer                |          |               |
## idelflg     | integer                |          |               |
## getu        | bigint                 |          |               |
## ka          | bigint                 |          |               |
## sui         | bigint                 |          |               |
## moku        | bigint                 |          |               |
## kin         | bigint                 |          |               |
## dou         | bigint                 |          |               |
## niti        | bigint                 |          |               |
## total       | bigint                 |          |               |
