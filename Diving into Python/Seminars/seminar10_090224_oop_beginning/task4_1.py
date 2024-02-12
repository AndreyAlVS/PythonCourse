# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

# через импорт

from task3 import DataPerson


class Employee(DataPerson):
    def __init__(self, name: str, surname: str, age: int, emp_id: int = 1):
        if len(str(emp_id)) != 6:
            raise ValueError('Некорректный идентификационный номер')
        self.emp_id = emp_id
        self.level = sum(map(int, str(emp_id))) % 7

        super().__init__(name, surname, age)


if __name__ == '__main__':
    e = Employee('Александр', 'Пушкин', 19, 123321)
    print(f'{e.emp_id=}, {e.level=}')