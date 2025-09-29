from .shapes import Shape

def calculate_area(shape: Shape) -> float:
    """
    Универсальная функция вычисления площади любой фигуры, реализующей интерфейс Shape.
    Позволяет вычислять площадь без знания типа фигуры во время компиляции.

    :param shape: Объект, наследник Shape.
    :return: Площадь фигуры.
    """
    return shape.area()
