# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

from random import randint
num = randint(0, 101)
print(f'Задано число {num}')

for i in range(1, num + 1):
    stepent = 2 ** i
    print(f'Два в степени {i} равно {stepent}')
