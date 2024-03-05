# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class DataPerson:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age  # __age - защищённая переменная (private)

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'ФИО: {self.surname} {self.name}, Возраст: {self.__age}'


person_1 = DataPerson('Ivan', 'Ivanov', 35)
person_2 = DataPerson('Petr', 'Petrov', 45)

print(DataPerson.full_name(person_1))
print(DataPerson.full_name(person_2))

