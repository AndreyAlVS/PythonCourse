# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно
#
#
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]


from random import randint


def selection(list1):
    for i in range(len(list1)):
        if left <= list1[i] <= right:
            select.append(list1.index(list1[i]))
    return select


list1 = [randint(1, 1000) for _ in range(10)]
print(list1)
left = int(input('Введите значение левой границы: '))
right = int(input('Введите значение правой границы: '))
select = []
selection(list1)
print(select)
