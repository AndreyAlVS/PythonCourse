import multiprocessing
counter = multiprocessing.Value('i', 0)


def increment(cnt):
    for _ in range(10_000):
        with cnt.get_lock():
            cnt.value += 1
    print(f'значение счетчика: {cnt.value:_}')


if __name__ == '__main__':
    process = []
    for i in range(5):
        p = multiprocessing.Process(target=increment, args=(counter,))
        process.append(p)
        p.start()

    for p in process:
        p.join()

    print(f'значение счетчика в финале: {counter.value:_}')
