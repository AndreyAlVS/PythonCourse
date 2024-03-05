# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

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


if __name__ == '__main__':
    c = DataNew('Hello', 'Joe')
    d = DataNew('Hello', 'David')

print(f'{c= }\t{c.old_text= }\t{type(c)}')
