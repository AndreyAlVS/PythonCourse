# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

s = 'Жили у бабуси два весёлых гуся'


def string_parse(string: str) -> str:
    data = string.split()
    data.sort()

    longest_word = len(max(data, key=len))

    res = ''
    for n, t in enumerate(data, 1):
        res += f'{n} {t:>{longest_word}}\n'

    return res


print(string_parse(s))
