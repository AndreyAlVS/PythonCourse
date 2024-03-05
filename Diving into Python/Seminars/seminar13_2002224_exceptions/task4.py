# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json
import os

#
# class User:
#     def __init__(self, id_: str, level: str, name: str):
#         self.id, self.level, self.name = id_, level, name
#
#
# # {1: {id: name}}
#
#
# def load_or_create(file_name: str):
#     if file_name in os.listdir():
#         with open(file_name, 'r', encoding='utf-8') as f:
#             data = json.load(f)
#             return data
#
#     with open(file_name, 'w') as f:
#         json.dump({}, f)
#     return {}
#
#
# def enter_users(level: str, id_: str, name: str, file_name: str) -> None:
#     data = load_or_create(file_name)
#     for value in data.values():
#         if id_ in value:
#             print('id exist')
#
#     data.setdefault(level, {})
#     data[level].setdefault(id_, name)
#
#     with open(file_name, 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=4)
#     return
#
#
# def load_users(file_name: str) -> set[User]:
#     data = load_or_create(file_name)
#     res = set()
#     for level, v in data.items():
#         for id_, name in v.items():
#             res.add(User(id_, level, name))
#     return res
#
#
# if __name__ == '__main__':
#     enter_users('5', '123456719', 'Alex', 's12task04data.json')
#     print(load_users('s12task04data.json'))


class User:
    def __init__(self, id_: str, level: str, name: str):
        self.id, self.level, self.name = id_, level, name


def __eq__(self, other):
    return self.id == other.id and self.name == other.name


def __hash__(self):
    return  hash(self.id)


def load_or_create(file_name: str):
    if file_name in os.listdir():
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    with open(file_name, 'w') as f:
        json.dump({}, f)
    return {}


def enter_users(level: str, id_: str, name: str, file_name: str) -> None:
    data = load_or_create(file_name)
    for value in data.values():
        if id_ in value:
            print("id уже существует")

    data.setdefault(level, {})
    data[level].setdefault(id_, name)

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    return


def load_users(file_name: str) -> set[User]:
    data = load_or_create(file_name)
    res = set()
    for level, v in data.items():
        for id_, name in v.items():
            res.add(User(id_, level, name))
    return res

if __name__ == '__main__':
    enter_users('5', '12345656', 'Alex', 'task04.json')
    enter_users('7', '12345657', 'Ben', 'task04.json')
    print(load_users('task04.json'))
