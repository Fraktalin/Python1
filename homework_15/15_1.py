import math

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_square(self) -> float:
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        total_area = self.get_square() + other.get_square()
        return Rectangle(self.width, round(total_area / self.width, 5))

    def __mul__(self, n: int) -> 'Rectangle':
        if not isinstance(n, (int, float)):
            raise ValueError("Множити можна тільки на число")
        new_area = self.get_square() * n
        return Rectangle(self.width, round(new_area / self.width, 5))

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert round(r3.get_square(), 5) == 26, 'Test3'

r4 = r1 * 4
assert round(r4.get_square(), 5) == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
