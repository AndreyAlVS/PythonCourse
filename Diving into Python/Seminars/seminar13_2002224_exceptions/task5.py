# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.


from task4 import User, load_users
from task3 import AccessError, LevelError, ProjectException


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


project1 = Project('task04.json')
project1.auth("12345656", "Alex")
# project1.auth("12345657", "Alex") # raise AccessError
project1.add_user("923456", "3", "Dima")  # raise LevelError
# project1.add_user("923456", "9", "Dima")
print(project1.data)
