# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform


def write_numbers(count_str: int, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        # my_str = f'{randint(-1000, 1000)}|{uniform(-1000, 1000)}\n'
        file.writelines([f'{randint(-1000, 1000)}|{uniform(-1000, 1000)}\n'
                         for _ in range(count_str)])


write_numbers(3, '12.txt')
