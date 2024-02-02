# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from random import randint, choice
from string import ascii_letters


def _name_file_generator(min_name, max_name):
    return ''.join([choice(ascii_letters)
                    for _ in range(randint(min_name, max_name))])


def write_file(
        ext='.txt',
        min_len_name=6,
        max_len_name=30,
        min_bytes=256,
        max_bytes=4096,
        count_files=42
) -> None:
    for i in range(count_files):
        with open(_name_file_generator(min_len_name, max_len_name) + ext, 'wb') as file:
            file.write(bytes([randint(0, 255)
                              for _ in range(randint(min_bytes, max_bytes))]))


write_file(count_files=3)
