# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

number = 1
numbers = [1, 2]
s = 's'


def get_attributes_end_with_s_() -> list:
    return list(filter(lambda v: not v.startswith('__')
                       and v.endswith('s')
                       and len(v) != 1, globals()))


print(f'{number=}, {numbers=}')

attributes_with_s_ = get_attributes_end_with_s_()

for attr in attributes_with_s_:
    globals()[attr[:-1]] = globals()[attr]
    globals()[attr] = None

print(f'{number=}, {numbers=}')
