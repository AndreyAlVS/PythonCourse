# Задача
# Необходимо создать функцию sumNumbers(n), которая будет
# считать сумму всех элементов от 1 до n.
# Решение:
#
# 1. Необходимо создать функцию:
# def sumNumbers(n):
# Очень важно понимать одну вещь, сколько аргументов мы передаем,
# столько и принимаем. Или наоборот сколько аргументов мы
# принимаем, столько и передаем.
# В нашем случае функция sumNumbers принимает 1 аргумент(n).

# variant 1
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     print(summa)
# sum_numbers(5)

# variant 2
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
# print(sum_numbers(5))

# variant 3
def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
a = sum_numbers(5)
print(a)


