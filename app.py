from flask import Flask, render_template, request, flash, redirect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from config import engine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

from models import *

Base.metadata.create_all(bind=engine)


# render_template-шаблонизатор во flask используется на основе jinja
# flash() – формирование сообщения пользователю;
# get_flashed_messages() – обработка сформированных сообщений в шаблоне документа.
# Их синтаксис, следующий:
#
# flask.flash(message, category=’message’)
#
# flask.get_flashed_messages(with_categories=False, category_filter=[])
#
# message – текст сообщения;
# category – категория сообщения;
# with_categories – разрешает использование категорий при извлечении сообщений;
# category_filter – список разрешенных категорий при выборке сообщений.


@app.route('/')
def index():
    return render_template('index.html', title="Главная")


@app.route('/settings/profile/<int:id>')
def profile(id):
    # Профиль
    item = Profile.query.get(id)
    return render_template('profile.html', title="Пользователь", item=item)


@app.route('/settings/profiles')
def profiles():
    # Список пользователей
    return render_template('profiles.html', title="Пользователи", items=Profile.query.all())


@app.route('/settings/create_profile', methods=["POST", "GET"])
def create_profile():
    # Регистрация пользователя
    if request.method == "POST":
        session.add(
            Profile(name=request.form['name'],
                    surname=request.form['surname'],
                    login=request.form['login'],
                    password=request.form['password'],
                    email=request.form['email']))
        session.commit()
        flash('Пользователь создан')
        return redirect('/settings/profiles')
    return render_template('create_profile.html', title="Создание пользователя")


@app.route('/login', methods=["POST", "GET"])
def login():
    # Логин
    return render_template('login.html', title="Логин")


@app.route('/settings/contragents', methods=["POST", "GET"])
def contragents():
    #     # Список контрагентов/Создание контрагентов
    if request.method == "POST":
        session.add(Contragent(**request.json))
        session.commit()
    return render_template('contragents.html', title="Контрагенты", items=Contragent.query.all())


@app.route('/settings/point/<int:id>', methods=["POST", "GET"])
def point(id):
    if request.method == "POST":
        for details in request.form.keys():
            session.query(Point).filter(Point.id == id).update({details: request.form[details]}, synchronize_session=False)
            session.commit()
        flash('адрес отредактирован')
        return redirect('/settings/points')
    return render_template('point.html', title="Точка", item=Point.query.get(id))


@app.route('/settings/points')
def points():
    # Список адресов
    return render_template('points.html', title="Точки", items=Point.query.all())


@app.route('/settings/create_point', methods=["POST", "GET"])
def create_point():
    # Регистрация адресов
    if request.method == "POST":
        session.add(Point(**request.form))
        session.commit()
        flash('Точка зарегистрирована')
        return redirect('/settings/points')
    return render_template('create_point.html', title="Создание точки")




if __name__ == '__main__':
    app.run(debug=True)

