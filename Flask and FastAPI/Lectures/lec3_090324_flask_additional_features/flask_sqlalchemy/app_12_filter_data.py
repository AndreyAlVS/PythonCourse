from datetime import datetime, timedelta

from flask import Flask, render_template, jsonify
from models import db, User, Post

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


@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('index.html', **context)


@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content,
              'created_at': post.created_at} for post in posts]
        )
    return jsonify({'error': 'Posts not found'}), 404


@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content,
              'created_at': post.created_at} for post in posts]
        )
    return jsonify({'error': 'Posts not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
