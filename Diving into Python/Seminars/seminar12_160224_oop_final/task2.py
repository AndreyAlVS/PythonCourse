# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.
import json
from collections import defaultdict


class Factorial:
    def __init__(self, size, name_file: str = 'json_file.json'):
        self.storage = defaultdict(int)
        self.size = size
        self.name_file = name_file

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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.name_file, 'w') as f_json:
            json.dump(self.storage, f_json, indent=4)
        self.storage.clear()


if __name__ == '__main__':
    ek = Factorial(5)
    with ek:

        for i in range(9):
            ek(i)
    print(f'{ek}')
