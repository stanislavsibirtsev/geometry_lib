import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Абстрактный базовый класс для всех фигур.
    Требует реализации метода area() для вычисления площади.
    """
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    """
    Класс круга с радиусом radius.
    """
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self) -> float:
        """
        Вычисляет площадь круга по формуле π * r^2.
        """
        return math.pi * self.radius ** 2


class Triangle(Shape):
    """
    Класс треугольника с тремя сторонами: a, b, c.
    """
    def __init__(self, a: float, b: float, c: float):
        # Проверяем валидность сторон треугольника
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны должны быть положительными")
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Такой треугольник не существует")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """
        Вычисляет площадь треугольника по формуле Герона:
        s = полупериметр
        площадь = sqrt(s(s-a)(s-b)(s-c))
        """
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angle(self) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным по теореме Пифагора.
        Стороны сортируются, затем проверяется равенство квадратов гипотенузы и суммы квадратов катетов.
        """
        sides = sorted([self.a, self.b, self.c])
        # math.isclose для точности работы с float
        return math.isclose(sides[2]**2, sides[0]**2 + sides[1]**2, rel_tol=1e-9)
