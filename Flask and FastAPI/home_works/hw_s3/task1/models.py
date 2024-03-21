# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Authors(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    student = db.relationship('Books', backref=db.backref('author'), lazy=True)

    def __repr__(self):
        return f'Authors({self.name})'


class Books(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year_of_publication = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id_'), nullable=False)

    def __repr__(self):
        return f'Books({self.title})'
