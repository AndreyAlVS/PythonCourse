import multiprocessing
import time


def worker(num):
    print(f'начало работы потока {num}')
    time.sleep(3)
    print(f'конец работы потока {num}')


if __name__ == '__main__':
    process = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        process.append(p)
        p.start()

    for p in process:
        p.join()

    print('Все процессы завершили работу')
