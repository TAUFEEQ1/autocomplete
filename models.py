from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String, nullable=False, index=True)
    lastname = db.Column(db.String, nullable=False, index=True)
    nin = db.Column(db.String, nullable=True)
    phone_no = db.Column(db.String, nullable=True)
    next_of_kin = db.Column(db.String, nullable=False)
    next_of_kin_phone_no = db.Column(db.String, nullable=False)
    district = db.Column(db.String, nullable=False)
    subcounty = db.Column(db.String, nullable=True)
    parish = db.Column(db.String, nullable=True)
    village = db.Column(db.String, nullable=True)
    residence = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False)
    latitude = db.Column(db.String, nullable=False)
    longitude = db.Column(db.String, nullable=False)
