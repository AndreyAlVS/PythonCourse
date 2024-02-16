# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    def __init__(self, leng, hgh=None):
        self.leng = leng
        self.hgh = hgh if hgh else leng  # Если в rectangle = Rectangle(10) передаём только одно значение,
        # То оно по умолчанию и ширина и высота (т.е. получаем квадрат.)

    def perimeter(self):
        return (self.leng + self.hgh) * 2

    def area(self):
        return self.leng * self.hgh

    def __add__(self, other: 'Rectangle'):
        new_perimetr = self.perimeter() + other.perimeter()
        new_length = self.leng + other.leng
        new_width = new_perimetr / 2 - new_length
        return Rectangle(new_length, new_width)

    def __str__(self):
        return f'Rectangle({self.leng=}, {self.hgh= })'

    def __sub__(self, other):
        new_perimetr = abs(self.perimeter() - other.perimeter())
        new_length = abs(self.leng - other.leng)
        new_width = new_perimetr / 2 - new_length
        if new_width < 0:
            return ValueError('Вычитание данных прямоугольника невозможно')
        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


if __name__ == '__main__':
    p1 = Rectangle(2, 10)
    p2 = Rectangle(3, 4)
    rectangle = Rectangle(10)
    print(rectangle.perimeter())
    print(rectangle.area())
    print(p1 + p2)
    print(p1 - p2)
    print(p1 == p2)
    print(p1 < p2)
    print(p1 <= p2)

