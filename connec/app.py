from flask import Flask, render_template,request,flash

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
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Главная")


@app.route('/settings')
def settings():
    return render_template('settings.html', title="Настр")


if __name__ == '__main__':
    app.run(debug=True)
