# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.
import time
import multiprocessing


def sum_array(arr, start, end):
    total = 0
    for i in range(start, end):
        total += arr[i]
    print(f'{'{:,}'.format(total)} ')


def main():
    with open('numbers.txt', 'r') as f:
        arr = [int(line.strip()) for line in f.readlines()]

    pool = multiprocessing.Pool(4)
    chunks = [arr[i:i + 250000] for i in range(0, len(arr), 250000)]
    tasks = [pool.apply_async(sum_array, (chunk, 0, len(chunk))) for chunk in chunks]
    for task in tasks:
        task.get()
        print(f"задача отработала за: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    start_time = time.time()
    main()
