# Задача для самостоятельного решения
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# моё решение:
#
# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# list2 = []
#
#
# for i in range(len(list1)):
#     if list1[i] % 2 == 0:
#         list2.append(list1[i])
#         sqare = list1[i] ** 2
#         list2.append(sqare)
#
#
# print(list2)

# решение лектора:

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data :
# if i % 2 == 0:
# out.append((i, i ** 2))
# print(out)

# решение лектора с лямбдой ф-цией:
def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
res = where(lambda x: x % 2 == 0, res)
print(res)  # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))
print(res)