# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
import time
from datetime import datetime


class MyString(str):
    def __new__(cls, my_string: str, *args, **kwargs):
        return super().__new__(cls, my_string)

    def __init__(self, *args, **kwargs):
        data, name, *_ = args
        self.data = data
        self.name = name
        self.time = datetime.now()


if __name__ == '__main__':
    s1 = MyString('string1', 'Author1')
    print(s1)
    s1.data = ''
    print(s1.__dict__)
