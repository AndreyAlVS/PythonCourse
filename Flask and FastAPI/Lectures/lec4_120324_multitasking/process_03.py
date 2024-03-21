import multiprocessing
counter = 0


def increment():
    global counter
    for _ in range(10_000):
        counter += 1
    print(f'значение счетчика: {counter:_}')


if __name__ == '__main__':
    process = []
    for i in range(5):
        p = multiprocessing.Process(target=increment)
        process.append(p)
        p.start()

    for p in process:
        p.join()

    print(f'значение счетчика в финале: {counter:_}')
