from api.database import db, ma

class Item(db.Model): 
    __tablename__ = "item" 
    id = db.Column(db.Integer, primary_key=True) 
    code = db.Column(db.String(), nullable=True) 
    name1 = db.Column(db.String(), nullable=True) 
    name2 = db.Column(db.String(), nullable=True) 
    tanka = db.Column(db.Integer, nullable=True) 
    orosine = db.Column(db.Integer, nullable=True) 
    zei_kb = db.Column(db.Integer, nullable=True) 
    del_flg = db.Column(db.Integer, nullable=True) 
    tenant_id   = db.Column(db.String(), primary_key=True) 

class ItemSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = Item
            load_instance = True

class VItemGroup(db.Model): 
    __tablename__ = "v_item_group" 
    min_id = db.Column(db.Integer, primary_key=True) 
    name1 = db.Column(db.String(), primary_key=False) 
    min_tanka = db.Column(db.Integer, primary_key=False) 
    max_tanka = db.Column(db.Integer, primary_key=False) 
    kensu = db.Column(db.Integer, primary_key=False) 
    tenant_id   = db.Column(db.String(), primary_key=True) 

class VItemGroupSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = VItemGroup
            load_instance = True
