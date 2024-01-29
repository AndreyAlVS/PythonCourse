# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

# моё решение:

# s = '1/2/3/4/7/8/9'.split('/')
#
#
# def dictionary(lst: list) -> dict:
#     new_dict = dict()
#     new_dict[lst[1]] = lst[0]
#     new_dict[lst[2]] = lst[3::]
#     return new_dict
#
#
# print(dictionary(s))

# решение на семинаре:

numbers = '1/2/3/4/5/6/7/8/9'
first, second, third, *forth = map(int, numbers.split('/'))
numb_dict = {second: first, third: tuple(forth)}
print(numb_dict)
