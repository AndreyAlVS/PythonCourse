import threading
import time


def worker(num):
    print(f'начало работы потока {num}')
    time.sleep(3)
    print(f'конец работы потока {num}')


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('Все потоки завершили работу')
