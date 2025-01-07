from .shape import Shape
from .point import Point

class Rectangle(Shape):
    def __init__(self, width, height):
        bottom_left = Point(0, 0)
        bottom_right = Point(width, 0)
        top_right = Point(width, height)
        top_left = Point(0, height)
        vertices = [bottom_left, bottom_right, top_right, top_left]
        super().__init__(vertices)
        self.width = width
        self.height = height

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)
