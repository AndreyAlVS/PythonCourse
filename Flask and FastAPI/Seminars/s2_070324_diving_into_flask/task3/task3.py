# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с ошибкой.
from flask import Flask, request, render_template

app = Flask(__name__)

LOGIN = 'admin'
PASSWD = '1234'


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('greet.html')
    get_login = request.form.get('login')
    get_passwd = request.form.get('passwd')

    if get_login == LOGIN and get_passwd == PASSWD:
        return render_template('index.html')
    return render_template('error.html')


if __name__ == '__main__':
    app.run()
