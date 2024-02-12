# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.


def count_decor(count: int):
    def decor(func):
        def wrapper(*args, **kwargs):
            res = []
            for _ in range(count):
                res.append(func(*args, **kwargs))
            return res
        return wrapper
    return decor


@count_decor(5)
def my_func(*args):
    return sum(args)


if __name__ == '__main__':
    print(my_func(4, 5, 8))
