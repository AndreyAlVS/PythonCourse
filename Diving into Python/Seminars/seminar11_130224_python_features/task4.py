# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

class DataNew:
    _instance = None

    def __new__(cls, text, name):
        # instance = super().__new__(cls, *, **)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.old_text = []
            cls._instance.old_name = []
        else:
            cls._instance.old_text.append(cls._instance.text)
            cls._instance.old_name.append(cls._instance.name)
        return cls._instance

    def __init__(self, text: str, name: str):
        self.name = name
        self.text = text

    def __str__(self):
        return f'{self.text} - {self.name}'

    def __repr__(self):
        return f'DataNew({self.text=}, {self.name=})'


if __name__ == '__main__':
    c = DataNew('Hello', 'Joe')
    d = DataNew('Hello', 'David')

print(f'{c= }\t{c.old_text= }\t{type(c)}')
print(repr(c))
