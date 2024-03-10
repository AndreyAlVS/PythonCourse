# 2. Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит: имя файла без расширения или название каталога, расширение, если это файл, флаг каталога,
# название родительского каталога. Написать 3-5 тестов к задаче.


import os
import argparse
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_file_info(file_path):
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    is_directory = os.path.isdir(file_path)
    parent_directory = os.path.basename(os.path.dirname(file_path))
    return FileInfo(name=file_name, extension=file_extension,
                    is_directory=is_directory, parent_directory=parent_directory)


def list_directory_contents(directory_path):
    directory_contents = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        directory_contents.append(get_file_info(item_path))
    return directory_contents


def main():
    parser = argparse.ArgumentParser(description='List information about files and directories in a given directory.')
    parser.add_argument('directory', metavar='DIRECTORY_PATH', type=str, help='Path to the directory')
    args = parser.parse_args()

    directory_path = args.directory

    if not os.path.isdir(directory_path):
        print("Error: Provided path is not a directory.")
        return

    contents = list_directory_contents(directory_path)
    for item in contents:
        print(item)


if __name__ == "__main__":
    main()
