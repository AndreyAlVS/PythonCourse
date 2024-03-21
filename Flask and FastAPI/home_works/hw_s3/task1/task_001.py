# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, render_template
from models import db, Authors, Books
from random import choice, randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///authors.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-author")
def add_author():
    for _ in range(1, 11):
        author = Authors(name=choice(['Hemingway', 'Marquez', 'Bradbury']))
        db.session.add(author)
    db.session.commit()

    for i in range(1, 11):
        book = Books(title=f'title{i}', year_of_publication=i + 1950,
                     quantity=1 + 100_000, author_id=randint(1, 10))
        db.session.add(book)
    db.session.commit()


@app.route('/')
def index():
    book = Books.query.all()
    return render_template('index.html', book=book)


if __name__ == '__main__':
    app.run(debug=True)
