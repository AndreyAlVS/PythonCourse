# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном списке урожайности грядки.

import random


def quantity_cones():
    for i in range(1, n + 1):
        cones = (random.randint(0, 101))
        print(f'На кусте № {i} выросло {cones} шишек')
        list1.append(cones)
    print(list1)


def crop_count():
    if bush == 1:
        harvest = list1[bush - 1] + list1[-1] + list1[bush]
    elif bush == len(list1):
        harvest = list1[bush - 1] + list1[0] + list1[bush - 2]
    else:
        harvest = list1[bush - 1] + list1[bush - 2] + list1[bush]
    return harvest


n = int(input('Введите кол-во кустов на грядке: '))
bush = int(input('Введите номер куста к которому нужно направить собирающий модуль: '))
list1 = []

quantity_cones()
print(f'Урожай составил {crop_count()} шишек')
print('Snoop Dogg одобряет' + '🚭')

# n = int(input('Введите кол-во кустов на грядке: '))
# bush = int(input('Введите номер куста к которому нужно направить собирающий модуль: '))
# cones = 0
# list1 = []
#
# for i in range(1, n + 1):
#     cones = (random.randint(0, 101))
#     print(f'На кусте № {i} выросло {cones} шишек')
#     list1.append(cones)
# print(list1)
#
# if bush == 1:
#     harvest = list1[bush - 1] + list1[-1] + list1[bush]
# elif bush == len(list1):
#     harvest = list1[bush - 1] + list1[0] + list1[bush - 2]
# else:
#     harvest = list1[bush - 1] + list1[bush - 2] + list1[bush]
#
#
# print(harvest
# print('Snoop Dogg happy' + '🚭')
