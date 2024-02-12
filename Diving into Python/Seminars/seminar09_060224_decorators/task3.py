# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json
import os
from typing import Callable


def json_cache(func: Callable) -> Callable:
    json_file = func.__name__ + '.json'
    json_data = {}

    if json_file not in os.listdir():
        with open(json_file, 'w') as f_init:
            json.dump(json_data, f_init)
    else:
        with open(json_file) as f:
            json_data = json.load(f)


    def wrapper(*args, **kwargs):
        key = f'{args=}, {kwargs=}'
        if key in json_data:
            return json_data[key]
        res = func(*args, **kwargs)
        json_data[key] = res
        with open(json_file, 'w') as f_out:
            json.dump(json_data, f_out, indent=2)
        return res
    return wrapper


@json_cache
def task3_func(*args, **kwargs):
    a, b, c, *_ = args
    return f'{a + b + c + sum(kwargs.values())}'


if __name__ == '__main__':
    task3_func(1, 2, 3, 4, 5, 6, 7, a=10, b=20, c=30)
    task3_func(2, 3, 4, 5, 6, 7, a=10, b=20, c=40)
    task3_func(3, 4, 5, 6, 7, a=10, b=20, c=50)
