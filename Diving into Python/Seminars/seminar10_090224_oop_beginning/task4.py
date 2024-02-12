# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

class Employee:
    def __init__(self, name: str, surname: str, ident: int, access_level=None):
        self.name = name
        self.surname = surname
        self.ident = ident
        self.access_level = access_level if access_level else sum(map(int, list(str(ident)))) % 7

    def employee(self):
        return f'{self.name} {self.surname}, {self.ident}, {self.access_level}'


person_1 = Employee('Ivan', 'Ivanov', 123456)
person_2 = Employee('Petr', 'Petrov', 789012)
print(person_1.employee())
print(person_2.employee())