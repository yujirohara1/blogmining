from api.database import db, ma
from datetime import datetime


## 実テーブル
class Seikyu(db.Model): 
    __tablename__ = "seikyu" 
    customer_id = db.Column(db.Integer, nullable=False,primary_key=True)
    deliver_ymd = db.Column(db.Integer, nullable=False,primary_key=True)
    item_id     = db.Column(db.Integer, nullable=False,primary_key=True)
    price       = db.Column(db.Integer, nullable=False,primary_key=True)
    price_sub   = db.Column(db.Integer, nullable=True) 
    quantity    = db.Column(db.Integer, nullable=False) 
    user_id     = db.Column(db.String(), nullable=False,primary_key=False)
    ymdt        = db.Column(db.DATETIME, nullable=False,primary_key=False)
    # ymdt        = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    # ymdt        = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow, nullable=False,primary_key=False)
    tenant_id   = db.Column(db.String(), primary_key=True) 
    

class SeikyuSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = Seikyu
            load_instance = True

## v_seikyu_a
class VSeikyuA(db.Model): 
    __tablename__ = "v_seikyu_a" 
    customer_id     = db.Column(db.Integer,  nullable=False,primary_key=True)
    nen             = db.Column(db.Integer,  nullable=False,primary_key=True)
    tuki            = db.Column(db.Integer,  nullable=False,primary_key=True)
    item_id         = db.Column(db.Integer,  nullable=False,primary_key=True)
    item_name1      = db.Column(db.String(), nullable=False,primary_key=False)
    price           = db.Column(db.Integer,  nullable=False,primary_key=False)
    price_sub       = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d01    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d02    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d03    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d04    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d05    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d06    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d07    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d08    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d09    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d10    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d11    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d12    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d13    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d14    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d15    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d16    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d17    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d18    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d19    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d20    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d21    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d22    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d23    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d24    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d25    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d26    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d27    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d28    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d29    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d30    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    quantity_d31    = db.Column(db.Integer,  nullable=True ,primary_key=False)
    item_name1_end  = db.Column(db.String(), nullable=True ,primary_key=False)
    tenant_id   = db.Column(db.String(), primary_key=True) 

class VSeikyuASchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = VSeikyuA
            load_instance = True


##                    テーブル"public.seikyu"
##     列      | タイプ  | 照合順序 | Null 値を許容 | デフォルト
##-------------+---------+----------+---------------+------------
## customer_id | integer |          |               |
## deliver_ymd | date    |          |               |
## item_id     | integer |          |               |
## price       | integer |          |               |
## price_sub   | integer |          |               |
## quantity    | integer |          |               |



##        列       |        タイプ         | 照合順序 | Null 値を許容 | デフォルト
## ----------------+-----------------------+----------+---------------+------------
##  customer_id    | integer               |          |               |
##  nen            | text                  |          |               |
##  tuki           | text                  |          |               |
##  item_id        | integer               |          |               |
##  item_name1     | character varying(80) |          |               |
##  price          | integer               |          |               |
##  price_sub      | integer               |          |               |
##  quantity_d01   | bigint                |          |               |
##  quantity_d02   | bigint                |          |               |
##  quantity_d03   | bigint                |          |               |
##  quantity_d04   | bigint                |          |               |
##  quantity_d05   | bigint                |          |               |
##  quantity_d06   | bigint                |          |               |
##  quantity_d07   | bigint                |          |               |
##  quantity_d08   | bigint                |          |               |
##  quantity_d09   | bigint                |          |               |
##  quantity_d10   | bigint                |          |               |
##  quantity_d11   | bigint                |          |               |
##  quantity_d12   | bigint                |          |               |
##  quantity_d13   | bigint                |          |               |
##  quantity_d14   | bigint                |          |               |
##  quantity_d15   | bigint                |          |               |
##  quantity_d16   | bigint                |          |               |
##  quantity_d17   | bigint                |          |               |
##  quantity_d18   | bigint                |          |               |
##  quantity_d19   | bigint                |          |               |
##  quantity_d20   | bigint                |          |               |
##  quantity_d21   | bigint                |          |               |
##  quantity_d22   | bigint                |          |               |
##  quantity_d23   | bigint                |          |               |
##  quantity_d24   | bigint                |          |               |
##  quantity_d25   | bigint                |          |               |
##  quantity_d26   | bigint                |          |               |
##  quantity_d27   | bigint                |          |               |
##  quantity_d28   | bigint                |          |               |
##  quantity_d29   | bigint                |          |               |
##  quantity_d30   | bigint                |          |               |
##  quantity_d31   | bigint                |          |               |
##  item_name1_end | character varying(80) |          |               |



# deliba_db=# \d v_seikyu_c
#                  ビュー"public.v_seikyu_c"
#     列    | タイプ  | 照合順序 | Null 値を許容 | デフォルト
# ----------+---------+----------+---------------+------------
#  nen      | text    |          |               |
#  tuki     | text    |          |               |
#  getugaku | numeric |          |               |
#  zeigaku  | numeric |          |               |

## v_seikyu_c

class VSeikyuC(db.Model): 
    __tablename__ = "v_seikyu_c" 
    nengetu         = db.Column(db.String(),  nullable=False,primary_key=True)
    getugaku        = db.Column(db.Integer,   nullable=True,primary_key=False)
    zeigaku         = db.Column(db.Integer,   nullable=True,primary_key=False)
    max_ymdt        = db.Column(db.String(),  nullable=True,primary_key=False)
    ninzu           = db.Column(db.Integer,   nullable=True,primary_key=False)
    tenant_id   = db.Column(db.String(), primary_key=True) 

class VSeikyuCSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = VSeikyuC
            load_instance = True



class VSeikyuB(db.Model): 
    __tablename__ = "v_seikyu_b" 
    nen             = db.Column(db.String(),  nullable=False,primary_key=True)
    tuki            = db.Column(db.String(),  nullable=False,primary_key=True)
    customer_id     = db.Column(db.Integer,   nullable=True,primary_key=True)
    list            = db.Column(db.Integer,   nullable=True,primary_key=True)
    group_id        = db.Column(db.Integer,   nullable=True,primary_key=False)
    name1           = db.Column(db.String(),  nullable=True,primary_key=False)
    zei_kb          = db.Column(db.String(),  nullable=True,primary_key=False)
    getugaku        = db.Column(db.Integer,   nullable=True,primary_key=False)
    zeigaku         = db.Column(db.Integer,   nullable=True,primary_key=False)
    max_ymdt        = db.Column(db.String(),  nullable=True,primary_key=False)
    tenant_id   = db.Column(db.String(), primary_key=True) 

class VSeikyuBSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = VSeikyuB
            load_instance = True




# deliba_db-# \d v_seikyu_b
#                           ビュー"public.v_seikyu_b"
#      列      |        タイプ         | 照合順序 | Null 値を許容 | デフォルト
# -------------+-----------------------+----------+---------------+------------
#  nen         | text                  |          |               |
#  tuki        | text                  |          |               |
#  group_id    | integer               |          |               |
#  list        | integer               |          |               |
#  customer_id | integer               |          |               |
#  name1       | character varying(80) |          |               |
#  zei_kb      | character varying(40) |          |               |
#  getugaku    | bigint                |          |               |
#  zeigaku     | integer               |          |               |
#  max_ymdt    | text                  |          |               |

