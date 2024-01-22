# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать как многочлен степени k.

#     *Пример:*

#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Input your degree: '))

coefficients = []
for _ in range(k + 1):
    coefficients.append(random.randint(0, 11))
result = ''

for i in range(len(coefficients) - 1):
    degree = len(coefficients) - i - 1
    if degree > 1:
        degree = f"*x^{degree}"
    elif degree == 1:
        degree = "*x"
    else:
        degree = ""
    if coefficients[i] > 1:
        result += f"{coefficients[i]}{degree} + "
    elif coefficients[i] == 1:
        result += f"{degree[1:]} + "

result += f"{coefficients[-1]} = 0"
print(coefficients)
print(result)