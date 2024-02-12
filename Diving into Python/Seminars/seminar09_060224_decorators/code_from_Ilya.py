import json
import os
from functools import wraps
from random import randint
from typing import Callable


def count_decor(count: int):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = []
            for _ in range(count):
                res.append(func(*args, **kwargs))
            return res

        return wrapper

    return decor


def json_cache(func: Callable) -> Callable:
    json_file = func.__name__ + '.json'
    json_data = {}

    if json_file not in os.listdir():
        with open(json_file, 'w') as f_init:
            json.dump(json_data, f_init)
    else:
        with open(json_file) as f:
            json_data = json.load(f)

    @wraps(func)
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


def value_checker(func):
    @wraps(func)
    def wrapper(number_secret, count):
        if not 1 <= number_secret <= 100:
            number_secret = randint(1, 100)
        if not 1 <= count <= 10:
            count = randint(1, 10)
        return func(number_secret, count)

    return wrapper


@json_cache
@count_decor(3)
@value_checker
def task05_run(number_secret: int, count: int):
    for _ in range(count):
        answer = int(input('Угадайте число: '))
        if number_secret == answer:
            return True
    return False


if __name__ == '__main__':
    task05_run(7, 2)