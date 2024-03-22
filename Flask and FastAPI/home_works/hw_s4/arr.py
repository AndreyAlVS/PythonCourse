import random

numbers = [random.randint(0, 100) for _ in range(1000000)]

with open('numbers.txt', 'w') as file:
    for number in numbers:
        file.write(str(number) + '\n')
