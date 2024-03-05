# На выбор ОДНО ИЗ ДВУХ ЗАДАНИЙ:
# 1. Взять класс студент из дз 12-го семинара,
# добавить запуск из командной строки(передача в качестве аргумента название csv-файла с предметами),
# логирование и написать 3-5 тестов с использованием pytest.
# 2. Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит: имя файла без расширения или название каталога, расширение, если это файл, флаг каталога,
# название родительского каталога. Написать 3-5 тестов к задаче.
#
# Сдавать дз ссылкой на репозиторий GitHub(проверьте что он не приватный перед отправкой).
#
# import csv
#
#
# class Student:
#     """
#     Класс, представляющий студента.
#
#     Атрибуты:
#     - name (str): ФИО студента
#     - subjects (dict): словарь, содержащий предметы и их оценки и результаты тестов
#
#     Методы:
#     - __init__(self, name, subjects_file): конструктор класса
#     - __setattr__(self, name, value): дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
#     - __getattr__(self, name): получение значения атрибута
#     - __str__(self): возвращает строковое представление студента
#     - load_subjects(self, subjects_file): загрузка предметов из файла CSV
#     - get_average_test_score(self, subject): возвращает средний балл по тестам для заданного предмета
#     - get_average_grade(self): возвращает средний балл по всем предметам
#     - add_grade(self, subject, grade): добавление оценки по предмету
#     - add_test_score(self, subject, test_score): добавление результата теста по предмету
#     """
#
#     def __init__(self, name, subjects_file):
#         self.name = name
#         self.subjects = {}
#         self.load_subjects(subjects_file)
#
#     def __setattr__(self, name, value):
#         if name == 'name':
#             if not value.replace(' ', '').isalpha() or not value.istitle():
#                 raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
#         super().__setattr__(name, value)
#
#     def __getattr__(self, name):
#         if name in self.subjects:
#             return self.subjects[name]
#         else:
#             raise AttributeError(f"Предмет {name} не найден")
#
#     def __str__(self):
#         return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"
#
#     def load_subjects(self, subjects_file):
#         with open(subjects_file, 'r') as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 subject = row[0]
#                 if subject not in self.subjects:
#                     self.subjects[subject] = {'grades': [], 'test_scores': []}
#
#     def add_grade(self, subject, grade):
#         if subject not in self.subjects:
#             self.subjects[subject] = {'grades': [], 'test_scores': []}
#         if not isinstance(grade, int) or grade < 2 or grade > 5:
#             raise ValueError("Оценка должна быть целым числом от 2 до 5")
#         self.subjects[subject]['grades'].append(grade)
#
#     def add_test_score(self, subject, test_score):
#         if subject not in self.subjects:
#             self.subjects[subject] = {'grades': [], 'test_scores': []}
#         if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
#             raise ValueError("Результат теста должен быть целым числом от 0 до 100")
#         self.subjects[subject]['test_scores'].append(test_score)
#
#     def get_average_test_score(self, subject):
#         if subject not in self.subjects:
#             raise ValueError(f"Предмет {subject} не найден")
#         test_scores = self.subjects[subject]['test_scores']
#         if len(test_scores) == 0:
#             return 0
#         return sum(test_scores) / len(test_scores)
#
#     def get_average_grade(self):
#         total_grades = []
#         for subject in self.subjects:
#             grades = self.subjects[subject]['grades']
#             if len(grades) > 0:
#                 total_grades.extend(grades)
#         if len(total_grades) == 0:
#             return 0
#         return sum(total_grades) / len(total_grades)
#
#
# # При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию
# # При отправке решения на Проверку закомментируйте эту строку обратно -
# # система автоматически подставит разные значения аргументов и вызовет функцию для проверки
#
# if __name__ == '__main__':
#     student = Student("Иван Иванов", "subjects.csv")
#     student.add_grade("Математика", 4)
#     student.add_test_score("Математика", 85)
#     student.add_grade("История", 5)
#     student.add_test_score("История", 92)
#     average_grade = student.get_average_grade()
#     print(f"Средний балл: {average_grade}")
#     average_test_score = student.get_average_test_score("Математика")
#     print(f"Средний результат по тестам по математике: {average_test_score}")
#     print(student)

import os
import argparse
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_file_info(file_path):
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    is_directory = os.path.isdir(file_path)
    parent_directory = os.path.basename(os.path.dirname(file_path))
    return FileInfo(name=file_name, extension=file_extension,
                    is_directory=is_directory, parent_directory=parent_directory)


def list_directory_contents(directory_path):
    directory_contents = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        directory_contents.append(get_file_info(item_path))
    return directory_contents


def main():
    parser = argparse.ArgumentParser(description='List information about files and directories in a given directory.')
    parser.add_argument('directory', metavar='DIRECTORY_PATH', type=str, help='Path to the directory')
    args = parser.parse_args()

    directory_path = args.directory

    if not os.path.isdir(directory_path):
        print("Error: Provided path is not a directory.")
        return

    contents = list_directory_contents(directory_path)
    for item in contents:
        print(item)


if __name__ == "__main__":
    main()
