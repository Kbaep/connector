from app import Base
import sqlalchemy as db


class Profile(Base):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

class Contragent(Base):
    __tablename__ = 'contragent'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    inn = db.Column(db.Integer, nullable=False)
    kpp = db.Column(db.Integer, nullable=True)
    kpp1 = db.Column(db.Integer, nullable=True)

class Point(Base):
    __tablename__ = 'point'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    gln = db.Column(db.Integer, nullable=False, unique=True)
    inn = db.Column(db.Integer, nullable=False)
    kpp = db.Column(db.Integer, nullable=False)
    index = db.Column(db.Integer, nullable=False)
    region_code = db.Column(db.Integer, nullable=False)
    area = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=True)
    locality = db.Column(db.String(255), nullable=True)
    side = db.Column(db.String(255), nullable=True)
    house = db.Column(db.String(255), nullable=True)
    frame = db.Column(db.String(255), nullable=True)
    flat = db.Column(db.String(255), nullable=True)