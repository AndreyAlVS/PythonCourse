# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя,
# а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти»,
# при нажатии на которую будет удалён cookie-файл с данными пользователя
# и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        response = make_response(redirect('/greet'))
        response.set_cookie('username', name)
        response.set_cookie('email', email)
        return response
    return redirect('/')


@app.route('/greet')
def greet():
    username = request.cookies.get('username')
    return render_template('greet.html', username=username)


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('email', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
