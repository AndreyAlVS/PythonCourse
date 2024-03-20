# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
#
# from flask_sqlalchemy import SQLAlchemy
# import enum
#
# db = SQLAlchemy()
#
#
# class Gender(enum.Enum):
#     male = 'Male'
#     female = 'Female'
#
#
# class Faculty(db.Model):
#     id_ = db.Column(db.Integer, primary_key=True)
#     fac = db.Column(db.String(80), nullable=False)
#     student = db.relationship('Student', backref=db.backref('faculty'), lazy=True)
#
#     def __repr__(self):
#         return f'Faculty({self.fac})'
#
#
# class Student(db.Model):
#     id_ = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     last_name = db.Column(db.String(80), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     gender = db.Column(db.Enum(Gender), nullable=False)
#     group = db.Column(db.Integer, nullable=False)
#     faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id_'), nullable=False)
#
#     def __repr__(self):
#         return f'Student({self.name}, {self.last_name})'

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()


class Gender(enum.Enum):
    male = 'муж'
    female = 'жен'


class Fags(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    fag_name = db.Column(db.String(80), nullable=False)
    student = db.relationship('Students', backref=db.backref('fags'), lazy=True)

    def __repr__(self):
        return f'Fags({self.fag_name})'


class Students(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    fags_id = db.Column(db.Integer, db.ForeignKey('fags.id_'), nullable=False)

    def __repr__(self):
        return f'Student({self.name}, {self.last_name})'
