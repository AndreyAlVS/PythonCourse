# Задача 10:
# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монеток на столе: "))

count = 0

for _ in range(n):
    coin = input("Монетка лежит вверх орлом (О) или решкой (Р): ")
    if coin == "О":
        count += 1

print(f"количество монет, которые нужно перевернуть: {count}")