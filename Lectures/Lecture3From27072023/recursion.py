# Рекурсия
#
# Рекурсия — это функция, вызывающая сама себя.
#
# давай рассмотрим следующую задачу:
# Пользователь вводит число n. Необходимо вывести n - первых
# членов последовательности Фибоначчи.
#
# Напоминание: Последовательно Фибоначчи, это такая последовательность, в
# которой каждое последующее число равно сумму 2-ух предыдущих.
#
# При описании рекурсии важно указать, когда функции надо остановиться и
# перестать вызывать саму себя. По-другому говоря, необходимо указать базис
# рекурсии

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)
