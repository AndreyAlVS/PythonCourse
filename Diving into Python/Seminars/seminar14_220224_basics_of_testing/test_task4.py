# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)


import pytest
from task2 import clear_text


def test_no_changes():
    assert clear_text('hello world') == 'hello world', 'Error'


def test_register():
    assert clear_text('Hello world') == 'hello world', 'Error'


def test_delete_punctuation():
    assert clear_text('Hello world!') == 'hello world', 'Error'


def test_delete_foreign_alphabet():
    assert clear_text('Hello мир!') == 'hello ', 'Error'


def test_all():
    assert clear_text('Hello, world или мир!') == 'hello world  ', 'Error'


if __name__ == '__main__':
    pytest.main()
