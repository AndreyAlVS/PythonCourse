# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов pytest для данного класса.


import pytest
from task5 import Rectangle


@pytest.fixture
def r1():
    return Rectangle(4, 8)


@pytest.fixture
def r2():
    return Rectangle(2, 4)


def test_init_rectangle():
    assert Rectangle(4, 8) is not None, 'Error'


def test_init_rectangle_incorrect():
    with pytest.raises(ValueError):
        Rectangle(-3, 5)


def test_is_area_int(r1):
    assert isinstance(r1.area(), int)


def test_add_is_rectangle(r1, r2):
    assert isinstance(r1 + r2, Rectangle)


if __name__ == '__main__':
    pytest.main(['-v'])
