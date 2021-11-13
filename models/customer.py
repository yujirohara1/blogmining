from api.database import db, ma

class Customer(db.Model): 
    __tablename__ = "customer" 
    __table_args__ = {'extend_existing': True} # 追記
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    name1       = db.Column(db.String(), nullable=False) 
    name2       = db.Column(db.String(), nullable=True) 
    address1    = db.Column(db.String(), nullable=True) 
    address2    = db.Column(db.String(), nullable=True) 
    address3    = db.Column(db.String(), nullable=True) 
    tel1        = db.Column(db.String(), nullable=True) 
    tel2        = db.Column(db.String(), nullable=True) 
    group_id    = db.Column(db.Integer,  nullable=False) 
    list        = db.Column(db.Integer,  nullable=True) 
    harai_kb    = db.Column(db.Integer,  nullable=False) 
    zei_kb      = db.Column(db.Integer,  nullable=False) 
    del_flg     = db.Column(db.Integer,  nullable=False) 
    biko1       = db.Column(db.String(), nullable=True) 
    biko2       = db.Column(db.String(), nullable=True) 
    biko3       = db.Column(db.String(), nullable=True) 
    tenant_id   = db.Column(db.String(), primary_key=True) 

class CustomerSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = Customer
            load_instance = True



class CustomerNentuki(db.Model): 
    __tablename__ = "customer" 
    __table_args__ = {'extend_existing': True} # 追記
    id          = db.Column(db.Integer, primary_key=True) 
    name1       = db.Column(db.String(), nullable=False) 
    name2       = db.Column(db.String(), nullable=True) 
    address1    = db.Column(db.String(), nullable=True) 
    address2    = db.Column(db.String(), nullable=True) 
    address3    = db.Column(db.String(), nullable=True) 
    tel1        = db.Column(db.String(), nullable=True) 
    tel2        = db.Column(db.String(), nullable=True) 
    group_id    = db.Column(db.Integer,  nullable=False) 
    list        = db.Column(db.Integer,  nullable=True) 
    harai_kb    = db.Column(db.Integer,  nullable=False) 
    zei_kb      = db.Column(db.Integer,  nullable=False) 
    del_flg     = db.Column(db.Integer,  nullable=False) 
    biko1       = db.Column(db.String(), nullable=True) 
    biko2       = db.Column(db.String(), nullable=True) 
    biko3       = db.Column(db.String(), nullable=True) 
    tenant_id   = db.Column(db.String(), primary_key=True) 
    kakute_ymdt = db.Column(db.DATETIME, nullable=True,primary_key=False)

class CustomerNentukiSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = CustomerNentuki
            load_instance = True

# id          | integer               |          | not null
# name1       | character varying(80) |          |
# name2       | character varying(80) |          |
# address1    | character varying(80) |          |
# address2    | character varying(80) |          |
# address3    | character varying(80) |          |
# tel1        | character varying(20) |          |
# tel2        | character varying(20) |          |
# group_id    | integer               |          |
# list        | integer               |          |
# keiyaku_ymd | date                  |          |
# start_ymd   | date                  |          |
# end_ymd     | date                  |          |
# stop_ymd    | date                  |          |
# harai_kb    | integer               |          |
# zei_kb      | integer               |          |
# del_flg     | integer               |          |
# biko1       | character varying(40) |          |
# biko2       | character varying(40) |          |
# biko3       | character varying(40) |          |