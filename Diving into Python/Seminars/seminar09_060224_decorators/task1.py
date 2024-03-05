# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
from random import randint


def game(num_secret: int, count: int):
    if not 1 <= num_secret <= 100:
        num_secret = randint(1, 100)
    if not 1 <= count <= 100:
        count = randint(1, 100)
    def run():
        for _ in range(count):
            answer = int(input('Devine num: '))
            if num_secret == answer:
                return True
        return False
    return run


if __name__ == '__main__':
    enter_ = game(5, 7)
    enter_()
