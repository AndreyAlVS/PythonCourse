# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
#
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

list_1 = [1, 2, 3, 4, 5]
k = 6
# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 10
# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8
# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11

differ = k - list_1[0]
neardig = 0
for i in list_1:
    dif = k - i
    if dif == 0:
        neardig = i
        break
    elif dif < 0:
        dif = (k - i) * -1
        if dif <= differ:
            differ = k - i
            neardig = i
    elif dif <= differ:
        differ = k - i
        neardig = i
print(neardig)
