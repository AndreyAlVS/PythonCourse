# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

s = 'why does my heart feel so good'

ord_dict = {i: ord(i) for i in s}
id = iter(ord_dict.items())
for _ in range(5):
    print(next(id))
