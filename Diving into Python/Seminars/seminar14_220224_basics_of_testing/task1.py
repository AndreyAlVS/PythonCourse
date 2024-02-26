# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters


def clear_text(s: str) -> str:
    chars = ascii_letters + ' '
    return ''.join([c for c in s if c in chars]).lower()


if __name__ == '__main__':
    print((clear_text('Hello world!')))
