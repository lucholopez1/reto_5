class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

    def compute_distance(self, point):
        return ((self._x - point.get_x()) ** 2 + (self._y - point.get_y()) ** 2) ** 0.5
