# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.
from collections import defaultdict


class Factorial:
    def __init__(self, size):
        self.storage = defaultdict(int)
        self.size = size

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return f'Объекты хранилища: \n{txt}'

    def __call__(self, k):
        f = 1
        for i in range(2, k + 1):
            f *= i
        if len(self.storage) == self.size:
            self.storage.pop(list(self.storage)[0])
        self.storage[k] = f
        return f


if __name__ == '__main__':
    ek = Factorial(5)
    print(ek(5))
    for i in range(9):
        ek(i)
        print(f'{ek}')
