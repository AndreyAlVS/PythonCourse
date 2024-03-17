from flask import Flask, request, render_template
from flask_wtf import CSRFProtect
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
# generation secrets key:
# in python console -> import secrets -> secrets.token_hex()
app.config['SECRET_KEY'] = b'696068ecbed9591d4bed6d00fa407cc02202f1b9dd3fe3c5b5c40a8f076a2464'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        print(email, password)
        ...
    return render_template('register.html', form=form)


# @app.route('/form', methods=['GET', 'POST'])
# def my_form():
# если форма без секретного ключа, создаем @csrf.exempt:
# @csrf.exempt
# def my_form():
#     ...
#     return 'No CSRF protection!'
# return


if __name__ == '__main__':
    app.run(debug=True)
