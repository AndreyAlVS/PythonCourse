# Напишите простое веб-приложение на Flask,
# которое будет выводить на экран текст "Hello, World!".

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello New Wonderful World!'


if __name__ == '__main__':
    app.run()
