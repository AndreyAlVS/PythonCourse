# Написать функцию, которая будет принимать на вход строку
# и выводить на экран ее длину.


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


@app.route('/length/<text>')
def length_text(text):
    return str(len(text))


if __name__ == '__main__':
    app.run(debug=True)
