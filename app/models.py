from . import db

class Property(db.Model):
    __tablename__ = "property"  # explicitly set table name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.String(20))
    property_type = db.Column(db.String(20))
    photo = db.Column(db.String(255))