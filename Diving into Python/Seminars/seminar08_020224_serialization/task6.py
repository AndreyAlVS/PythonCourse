# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv

def pickle_to_csv(pk_file, csv_file):
    with open(pk_file, 'rb') as source:
        data = pickle.load(source)
    with open(csv_file, 'w', newline='') as out:
        writer = csv.DictWriter(out, data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    pickle_to_csv('data.pickle', 'data.csv')

