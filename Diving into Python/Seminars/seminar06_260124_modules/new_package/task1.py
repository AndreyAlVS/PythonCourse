# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь

import random


def guessing_game(min_number, max_number, count):
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


if __name__ == '__main__':
    print(guessing_game(1, 10, 3))
