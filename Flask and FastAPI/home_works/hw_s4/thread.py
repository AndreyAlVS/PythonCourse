# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

import time
from concurrent.futures import ThreadPoolExecutor


def sum_array(arr, start, end):
    total = 0
    for i in range(start, end):
        total += arr[i]
    print(f'{'{:,}'.format(total)} ')


def main():
    with open('numbers.txt', 'r') as f:
        arr = [int(line.strip()) for line in f.readlines()]

    with ThreadPoolExecutor(max_workers=4) as executor:
        chunks = [arr[i:i + 250000] for i in range(0, len(arr), 250000)]
        tasks = [executor.submit(sum_array, chunk, 0, len(chunk)) for chunk in chunks]
        for task in tasks:
            task.result()
            print(f"поток отработал за: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    start_time = time.time()
    main()
