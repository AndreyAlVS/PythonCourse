# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# Последовательность Фибоначчи: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci_find(n) -> int:
    if n == 0 or n == 1:
        return n
    # if n in (1, 2):
    #     return 1
    return fibonacci_find(n - 1) + fibonacci_find(n - 2)


print(fibonacci_find(int(input('Input the position of your number: '))))
