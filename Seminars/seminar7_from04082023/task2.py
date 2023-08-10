# Задача №49.
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна.

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10


import math


def find_farthest_orbit(list_of_orbits):
    edited_list = list(filter(lambda item: item[0] != item[1], list_of_orbits))
    s_list = list(map(lambda item: item[0]*item[1]*math.pi, edited_list))
    return list_of_orbits.index(edited_list[s_list.index(max(s_list))])


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(f'Index of farthest planet: {find_farthest_orbit(orbits)}')


# import math
#
#
# def find_farthest_orbit(orbits, biggest_orbit):
#     for i in range(len(orbits[-2])):
#         s = math.pi * orbits[i] * orbits[i+1]
#         if s > biggest_orbit:
#             biggest_orbit = s
#     return biggest_orbit
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# biggest_orbit = 0
# print(find_farthest_orbit(orbits, biggest_orbit))
