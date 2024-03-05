# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.


from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

description = ['blablabla', 'blabla', 'bla']
something_more = ['blablabla', 'blabla', 'bla']


@app.route('/')
def index():
    return render_template('index.html', title='main', description=description,
                           something_more=something_more)


@app.route('/foots/')
def foots():
    return render_template('foots.html', title='foots')


@app.route('/hats/')
def hats():
    print(url_for('hats'))
    return render_template('hats.html', title='hats')


@app.route('/jackets/')
def jackets():
    print(url_for('jackets'))
    return render_template('jackets.html', title='jackets')


@app.route('/pos/')
def pos():
    print(url_for('pos'))
    return render_template('pos.html', title='pos')


if __name__ == '__main__':
    app.run(debug=True)
