# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов
from random import randint


def game(func):
    def wrapper(num_secret: int, count: int):
        if not 1 <= num_secret <= 100:
            num_secret = randint(1, 100)
        if not 1 <= count <= 100:
            count = randint(1, 100)
        return func(num_secret, count)
    return wrapper


@game
def run(num_secret: int, count: int):
    for _ in range(count):
        answer = int(input('Devine num: '))
        if num_secret == answer:
            return True
    return False


if __name__ == '__main__':
    run(7, 10)
