from datetime import datetime
from gtcs_Stock import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    phn_number = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.location}', '{self.phn_number}')"


class NewCompany(UserMixin, db.Model):
    comp_name = db.Column(db.String(20), primary_key=True)
    website = db.Column(db.String(20), nullable=False)
    regd_address = db.Column(db.String(20), nullable=False)
    work_address = db.Column(db.String(20), nullable=False)
    type_of_business = db.Column(db.String(20), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    vat = db.Column(db.Integer, nullable=False)
    tin = db.Column(db.Integer, nullable=False)
    gstin = db.Column(db.Integer, nullable=False)
    cin = db.Column(db.Integer, nullable=False)
    pan = db.Column(db.Integer, nullable=False)
    service_tax = db.Column(db.Integer, nullable=False)
    mfg = db.Column(db.Integer, nullable=False)
    dl = db.Column(db.Integer, nullable=False)
    telephone = db.Column(db.Integer, nullable=False)
    fax = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.comp_name}', '{self.website}')"


class ItemMaster(UserMixin, db.Model):
    item_barcode = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(20), nullable=False)
    item_model = db.Column(db.String(20), nullable=False)
    godown = db.Column(db.String(20), nullable=False)
    purchase = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    min_stock = db.Column(db.Integer, nullable=False)
    open_stock = db.Column(db.String(20), nullable=False)
    gst = db.Column(db.Integer, nullable=False)
    lot_no = db.Column(db.Integer, nullable=False)
    hsn = db.Column(db.Integer, nullable=False)
    batch = db.Column(db.Integer, nullable=False)
    mfg = db.Column(db.String(20), nullable=False)
    expire = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"ItemMaster('{self.item_barcode}', '{self.item_name}', '{self.desc}')"

class RateMaster(UserMixin, db.Model):
    material_code = db.Column(db.String(20), primary_key=True)
    material = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    sale_rate = db.Column(db.Integer, nullable=False)
    mrp = db.Column(db.Integer, nullable=False)
    purchase_unit = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"RateMaster('{self.material_code}', '{self.material}', '{self.desc}')"

class UnitMaster(UserMixin, db.Model):
    unit_code = db.Column(db.String(20), primary_key=True)
    unit = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"UnitMaster('{self.unit_code}', '{self.unit}', '{self.desc}')"