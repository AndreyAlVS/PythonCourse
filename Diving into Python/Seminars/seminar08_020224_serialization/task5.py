# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import os
import pickle


def save_json_to_pickle(path_in: str):
    ext = '.json'
    os.chdir(path_in)
    for file in os.listdir():
        if not file.endswith(ext):
            continue
        pickle_out, _ = file.split('.')
        with (
            open(file, 'r') as f_in,
            open(f'{pickle_out}.pickle', 'wb') as f_out,
        ):
            pickle.dump(json.load(f_in), f_out)


if __name__ == '__main__':
    save_json_to_pickle(r'C:\Users\Мой ПК\Desktop\GB разработчик\PythonCourse\Diving into Python\Seminars\seminar08_020224_serialization')
