# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)


def get_special_count(array: list):
    count = 0
    for i in range(0, len(array)):
        if i == len(array) - 1:
            if array[i - 1] < array[i] and array[0] < array[i]:
                count += 1
        else:
            if array[i - 1] < array[i] and array[i + 1] < array[i]:
                count += 1
    return count


def check_neighbors(index, sp: list):
    mid = sp[index]
    left = sp[index-1]
    if index == len(sp)-1:
        right = sp[0]
    else:
        right = sp[index+1]
    return int(mid > left and mid > right)


current_list = [5, 1, 3, 2, 5, 4]

res = [check_neighbors(index, current_list) for index in range(len(current_list))]

print(current_list)
# print(get_special_count(current_list))
print(sum(res))
