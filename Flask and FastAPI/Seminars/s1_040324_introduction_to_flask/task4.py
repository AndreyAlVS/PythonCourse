# Написать функцию, которая будет выводить на экран HTML страницу
# с заголовком "Моя первая HTML страница" и абзацем "Привет, мир!".


from flask import Flask

app = Flask(__name__)

html = """
<h1>"Моя первая HTML страница"</h1>
<p>"Привет, мир!"</p>
"""


@app.route('/web/')
def web():
    return html


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
