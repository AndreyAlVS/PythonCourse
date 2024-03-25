import os
import pytest
import shutil
from collections import Counter
from task1 import list_directory_contents


@pytest.fixture
def existing_test_directory(tmpdir):
    """Создаеем временный каталог для выполнения тестов,
    копируем файлы и каталоги из проверяемого каталога"""
    temp_dir = tmpdir.mkdir("existing_test_dir")
    source_dir = r"C:\Users\omaks\Desktop\GeekBrains\Python_5\Seminar_15"  # путь до проверяемого каталога
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        if os.path.isfile(source_item):
            shutil.copy(source_item, temp_dir)
        elif os.path.isdir(source_item):
            shutil.copytree(source_item, os.path.join(temp_dir, item))

    return temp_dir


def test_list_directory_contents(existing_test_directory):
    """Проверка наличия файлов и каталогов в директории"""
    temp_dir = existing_test_directory
    contents = list_directory_contents(temp_dir)
    assert len(contents) == len(os.listdir(temp_dir))


def test_file_extensions_count(existing_test_directory):
    """Вывод информации о количестве файлов для каждого расширения в директории"""
    temp_dir = existing_test_directory
    files = [file for file in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, file))]
    file_extensions = [os.path.splitext(file)[1] for file in files]
    extension_count = Counter(file_extensions)

    # Print information about file extensions and their counts
    for extension, count in extension_count.items():
        print(f"Files with extension '{extension}' found: {count}")


def test_max_file_limit(existing_test_directory):
    """Проверка допустимого количества файлов в диретории"""
    temp_dir = existing_test_directory
    if len(os.listdir(temp_dir)) > 100:
        with pytest.raises(ValueError) as excinfo:
            list_directory_contents(temp_dir)
        assert str(excinfo.value) == "В директории допускается хранение не более 100 файлов"


if __name__ == '__main__':
    pytest.main()