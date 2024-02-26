# Cоздайте класс с базовым исключением и дочерние классы-исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

from task4 import User


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
