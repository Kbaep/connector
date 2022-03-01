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
    kpp = db.Column(db.Integer, default='null', nullable=False)