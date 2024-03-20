from flask import Flask, render_template
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data'


@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
