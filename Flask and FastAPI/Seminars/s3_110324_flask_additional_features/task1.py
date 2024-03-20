# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.
#
# from flask import Flask, render_template
# from models import db, Student, Faculty, Gender
# from random import choice, randint
#
# app = Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_task1.db'
# db.init_app(app)
#
#
# @app.route('/')
# def index():
#     return 'Hi!'
#
#
# @app.cli.command('init-db')
# def init_db():
#     db.create_all()
#     print('ok')
#
#
# @app.cli.command('add-student')
# def add_student():
#     for i in range(1, 11):
#         faculty = Faculty(fac=choice(['math', 'hist', 'lang']))
#         db.session.add(faculty)
#     db.session.commit()
#
#     for i in range(1, 11):
#         student = Student(name=f'name{i}', last_name=f'last_name{i}', age=i + 15,
#                           gender=choice([Gender.male, Gender.female]),
#                           group=choice([1, 2, 3]), faculty_id=randint(1, 10))
#         db.session.add(student)
#     db.session.commit()
#
#
# @app.cli.command('edit-john')
# def edit_user():
#     user = User.query.filter_by(username='john').first()
#     user.email = 'new_email@example.com'
#     db.session.commit()
#     print('Edit John mail in DB!')
#
#
# @app.cli.command('del-john')
# def del_user():
#     user = User.query.filter_by(username='john').first()
#     db.session.delete(user)
#     db.session.commit()
#     print('Del John from DB!')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
from models import db, Students, Fags, Gender
from random import choice, randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task1_db.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-user")
def add_user():
    for _ in range(1, 11):
        fag = Fags(fag_name=choice(['math', 'hist', 'lang']))
        db.session.add(fag)
    db.session.commit()

    for i in range(1, 11):
        student = Students(name=f'name{i}', last_name=f'last_name{i}', age=i + 15,
                           gender=choice([Gender.male, Gender.female]),
                           group=choice([1, 2, 3]), fags_id=randint(1, 10))
        db.session.add(student)
    db.session.commit()


@app.route('/')
def index():
    student = Students.query.all()
    return render_template('index.html', student=student)


if __name__ == '__main__':
    app.run(debug=True)
