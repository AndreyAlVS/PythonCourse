# Задача № 45.
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
#
# Ввод:
# 300
#
# Вывод:
# 220 284


def sum_of_divisors(n) -> int:
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum


def find_friendly_numbers(k) -> list[tuple[int, int]]:
    friendly_pairs = []

    for n in range(1, k + 1):
        m = sum_of_divisors(n)
# if m <= k and sum_of_divisors(m) == n and m != n and (n, m) not in friendly_pairs and (m, n) not in friendly_pairs:
        if m < n and sum_of_divisors(m) == n:
            pair = (n, m)
            friendly_pairs.append(pair)
    return friendly_pairs


k = int(input("Введите число k: "))
pairs = find_friendly_numbers(k)

for pair in pairs:
    print(pair[0], pair[1])
