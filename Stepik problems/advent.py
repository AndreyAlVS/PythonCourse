# advent1 = [4, 8, 15, 16, 3, 14, 15, 192, 168, 1992, 37, 256, 98, 'x', 'x']
# #         -    lOST    -    Pi   -
# advent2 = [7787, 918, 39, 1098, 222, 69, 96, 5234, 777]

# 0) Соберите все полученные из задач числа в список. Список должен состоять из 24 положительных целых чисел.
# 1) Все четные элементы полученного списка следует заменить на их квадраты.
# 2) Все нечетные элементы полученного списка следует удвоить (умножить на два).
# 3) Выкиньте все лишнее, а именно числа, которые делятся нацело на 24 (ходят слухи, что Санта не переносит это число).
# 4) Из оставшихся чисел составьте наибольшее и наименьшее числа (см. пояснение).
#    Запишите их значения в переменные max_number и min_number соответственно.
# 5) Ответом на задачу является значение выражения max_number + min_number.
#
# Пояснение. Если список, полученный после третьего шага, содержал бы числа [4, 12, 13, 78],
# то мы бы составили наибольшее число max_number = 7841312, а наименьшее число — min_number = 1213478.

advent = [4, 8, 15, 16, 3, 14, 15, 192, 168, 1992, 37, 256, 98, 101, 273, 7787, 918, 39, 1098, 222, 69, 96, 5234, 777]
sqr = []

for i in range(len(advent)):
    if advent[i] % 2 == 0:
        sqr.append(advent[i]*advent[i])
    else:
        sqr.append(advent[i]*2)
print(sqr)


def filter_odd_num(sqr):
    if(sqr % 24) == 0:
        return False
    else:
        return True


out_filter = filter(filter_odd_num, sqr)
print(list(out_filter))

max_number = 960484272478746655366454649284303027394756256202196161557415541381205604
min_number = 120560413815541557416196202256273947563030492845466465536674788427249604
res = max_number + min_number
print(res)


