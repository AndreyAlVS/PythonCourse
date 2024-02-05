# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint, choice

VOWELS = 'aoeiuy'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'


def _name_generator():
    return ''.join([choice(CONSONANTS) if i % 2 != 0 else choice(VOWELS)
                    for i in range(randint(4, 7))]).capitalize()


def pseudo_names(count_str: int, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines([_name_generator() + '\n' for _ in range(count_str)])


pseudo_names(10, 'names.txt')
