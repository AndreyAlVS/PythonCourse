# Добавьте две дополнительные страницы в ваше веб-приложение: страницу "about" и страницу "contact".
# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello New Wonderful World!'


@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'


@app.route('/number/<int:num1>/<int:num2>')
def summ(num1, num2):
    return str(num1 + num2)


if __name__ == '__main__':
    app.run(debug=True)
