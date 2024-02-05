# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

from random import randint, uniform, choice

VOWELS = 'aoeiuy'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'


def write_numbers(count_str: int, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        # my_str = f'{randint(-1000, 1000)}|{uniform(-1000, 1000)}\n'
        file.writelines([f'{randint(-1000, 1000)}|{uniform(-1000, 1000)}\n'
                         for _ in range(count_str)])


def _name_generator():
    return ''.join([choice(CONSONANTS) if i % 2 != 0 else choice(VOWELS)
                    for i in range(randint(4, 7))]).capitalize()


def pseudo_names(count_str: int, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines([_name_generator() + '\n' for _ in range(count_str)])


def my_readline(file):
    line = file.readline()
    if line == '':
        file.seek(0)
        return file.readline()
    return line


def write_with_join(names_source, numbers, result_name) -> None:
    with (open(names_source, 'r') as name,
          open(numbers, 'r') as numb,
          open(result_name, 'w') as res):
        len_name = len(name.read().split('\n'))
        len_numb = len(numb.read().split('\n'))
        max_len = max(len_name, len_numb)

        for i in range(max_len - 1):
            new_name = my_readline(name).replace('\n', '')
            new_int, new_float = my_readline(numb).replace('\n', '').split('|')
            new_numb = int(new_int) * float(new_float)
            if new_numb < 0:
                res.write(f'{new_name.lower()} {abs(new_numb)}\n')
            else:
                res.write(f'{new_name.upper()} {int(new_numb)}\n')


write_numbers(5, '12.txt')
pseudo_names(5, 'names.txt')
write_with_join('12.txt', 'names.txt', 'result.txt')
