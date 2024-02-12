# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.
class Rectangle:
    def __init__(self, leng, hgh=None):
        self.leng = leng
        self.hgh = hgh if hgh else leng  # Если в rectangle = Rectangle(10) передаём только одно значение,
        # То оно по умолчанию и ширина и высота (т.е. получаем квадрат.)

    def perimeter(self):
        return (self.leng + self.hgh) * 2

    def area(self):
        return self.leng * self.hgh


rectangle = Rectangle(10)
print(rectangle.perimeter())
print(rectangle.area())
