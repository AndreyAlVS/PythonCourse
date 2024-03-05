import json
import os


class User:
    def __init__(self, id_: str, level: str, name: str):
        self.id, self.level, self.name = id_, level, name


def __eq__(self, other):
    return self.id == other.id and self.name == other.name


def __hash__(self):
    return hash(self.id)


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


class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    def __init__(self, new_lvl, adm_lvl):
        self.new_lvl, self.adm_lvl = new_lvl, adm_lvl

    def __str__(self):
        return f'Уровень пользователя {self.new_lvl} меньше, чем ваш уровень {self.adm_lvl}.'


class AccessError(ProjectException):
    def __init__(self, user: User):
        self.user = user

    def __str__(self):
        return f'Такого пользователя {self.user} нет.'


class Project:
    def __init__(self, file_name):
        self.data = load_users(file_name)
        self.admin = None

    def auth(self, id_, name):
        user_temp = User(id_, '', name)
        if user_temp not in self.data:
            raise AccessError(user_temp)
        for user in self.data:
            if user == user_temp:
                self.admin = user

    def add_user(self, id_, level, name):
        if not self.admin:
            raise ProjectException
        if int(level) < int(self.admin.level):
            raise LevelError(level, self.admin.level)
        self.data.add(User(id_, level, name))
