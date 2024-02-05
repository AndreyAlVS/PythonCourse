# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
import pathlib
import os


def sort_files():
    curr_path = pathlib.Path(os.getcwd())
    for file in curr_path.iterdir():
        if file.suffix == '.py':
            continue
        try:
            file.replace(f'{file.suffix}/{file.name}')
        except FileNotFoundError:
            os.mkdir(file.suffix)
            file.replace(f'{file.suffix}/{file.name}')


if __name__ == '__main__':
    sort_files()
