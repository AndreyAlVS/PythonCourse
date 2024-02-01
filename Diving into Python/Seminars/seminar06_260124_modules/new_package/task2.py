# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение

import random
from sys import argv


def guessing_game(min_number=5, max_number=10, count=3):
    gen_numb = random.randint(min_number, max_number)
    for i in range(count):
        numb = int(input('Enter number: '))
        if gen_numb == numb:
            return True
        elif gen_numb > numb:
            print('больше')
        else:
            print('меньше')
    return False


print(argv)
if __name__ == '__main__':
    print(guessing_game(*list(map(int, argv[1:]))))
