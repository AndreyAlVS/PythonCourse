# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

import logging


def log_decor(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename=f'{func.__name__}.log', encoding='utf-8', level=logging.DEBUG)
        res = func(*args, **kwargs)
        logging.debug(f'{args} {kwargs} {res}')
        return

    return wrapper


@log_decor
def division(x: int | float, y: int | float):
    try:
        return x / y
    except ZeroDivisionError as err:
        return float('inf')


if __name__ == '__main__':
    division(2, 5)
