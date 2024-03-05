from random import randint
import json
import os
from typing import Callable
from functools import wraps


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
    def wrapper(num_secret: int, count: int):
        if not 1 <= num_secret <= 100:
            num_secret = randint(1, 100)
        if not 1 <= count <= 100:
            count = randint(1, 100)
        return func(num_secret, count)
    return wrapper


@json_cache
@count_decor(3)
@value_checker
def task05_run(num_secret: int, count: int):
    for _ in range(count):
        answer = int(input('Devine num: '))
        if num_secret == answer:
            return True
    return False


if __name__ == '__main__':
    task05_run(7, 2)
