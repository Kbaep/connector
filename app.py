from flask import Flask, request, jsonify
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import engine


app = Flask(__name__)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

from models import *

# Base.metadata.create_all(bind=engine)

@app.route('/')
def index():
    return 'Главная страница'


@app.route('/settings')
def settings():
    return 'Настройки'





if __name__ == '__main__':
    app.run(debug=True)
