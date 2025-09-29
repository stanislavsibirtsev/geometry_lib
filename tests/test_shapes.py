import unittest
import math
from geometry_lib.shapes import Circle, Triangle
from geometry_lib.utils import calculate_area

class TestShapes(unittest.TestCase):
    """
    Класс тестов для проверки корректности работы фигур из geometry_lib.shapes
    и функции вычисления площади из geometry_lib.utils.
    """

    def test_circle_area(self):
        """Тест площади круга и валидации радиуса."""
        c = Circle(1)
        self.assertAlmostEqual(c.area(), math.pi, places=7)  # Площадь круга с радиусом 1 равна π
        with self.assertRaises(ValueError):
            Circle(0)  # Радиус не может быть 0

    def test_triangle_area(self):
        """Тест площади треугольника и проверки валидности сторон."""
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6.0)  # Площадь известного прямоугольного треугольника 3-4-5 равна 6
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)  # Стороны не могут образовывать треугольник
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 2)  # Отрицательная сторона

    def test_triangle_right_angle(self):
        """Проверка метода определения прямоугольного треугольника."""
        right_triangle = Triangle(3, 4, 5)
        self.assertTrue(right_triangle.is_right_angle())
        non_right_triangle = Triangle(3, 3, 3)
        self.assertFalse(non_right_triangle.is_right_angle())

    def test_calculate_area_func(self):
        """Проверка универсальной функции вычисления площади по объекту Shape."""
        c = Circle(2)
        t = Triangle(2, 2, 3)
        self.assertAlmostEqual(calculate_area(c), math.pi * 4)
        self.assertAlmostEqual(calculate_area(t), t.area())

if __name__ == "__main__":
    unittest.main()
