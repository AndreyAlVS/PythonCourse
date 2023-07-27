# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random


def first_numkit():
    nums_kit1 = []
    for _ in range(n):
        nums_kit1.append(random.randint(0, 15))
    print(f'Первый набор чисел: {nums_kit1}')
    nums_set1 = set(nums_kit1)
    return nums_set1


def second_numkit():
    nums_kit2 = []
    for _ in range(m):
        nums_kit2.append(random.randint(0, 15))
    print(f'Второй набор чисел: {nums_kit2}')
    nums_set2 = set(nums_kit2)
    return nums_set2


n = int(input('Введите размер первого набора чисел: '))
m = int(input('Введите размер второго набора чисел: '))
final_set = first_numkit() | second_numkit()
final_kit = list(final_set)
print(f'Упорядоченный набор неповторяющихся, целых чисел, встречающихся в обоих наборах:{final_kit}')


# def first_numkit():
#     nums_kit1 = []
#     for _ in range(n):
#         nums_kit1.append(random.randint(0, 31))
#     print(f'Первый набор чисел: {nums_kit1}')
#
#     return nums_kit1
#
#
# def second_numkit():
#     nums_kit2 = []
#     for _ in range(m):
#         nums_kit2.append(random.randint(0, 31))
#     return nums_kit2
#
#
#
# def fin_kit():
#     nums_set1 = set(first_numkit())
#     nums_set2 = set(second_numkit())
#     final_set = nums_set1 | nums_set2
#     final_kit = list(final_set)
#     return final_kit
#
#
# n = int(input('Введите размер первого набора чисел: '))
# m = int(input('Введите размер второго набора чисел: '))
# print(f'Первый набор чисел: {first_numkit()}')
# print(f'Второй набор чисел: {second_numkit()}')
# print(f'Упорядоченный набор неповторяющихся, целых чисел, встречающихся в обоих наборах:{fin_kit()}')

# n = int(input('Введите размер первого набора чисел: '))
# nums_kit1 = []
# for _ in range(n + 1):
#     nums_kit1.append(random.randint(0, 31))
# m = int(input('Введите размер второго набора чисел: '))
# nums_kit2 = []
# for _ in range(m + 1):
#     nums_kit2.append(random.randint(0, 31))
#
# print(f'Первый набор чисел: {nums_kit1}')
# print(f'Второй набор чисел: {nums_kit2}')
#
# nums_set1 = set(nums_kit1)
# nums_set2 = set(nums_kit2)
#
# final_set = nums_set1 | nums_set2
#
# final_kit = list(final_set)
#
# print(f'Упорядоченный набор,неповторяющихся целых чисел,встречающихся в обоих наборах:{final_kit}'
