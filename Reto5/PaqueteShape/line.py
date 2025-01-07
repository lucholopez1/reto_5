from .point import Point

class Line:
    def __init__(self, start_point, end_point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self.compute_length()

    def get_start_point(self):
        return self._start_point

    def set_start_point(self, point):
        self._start_point = point
        self._length = self.compute_length()

    def get_end_point(self):
        return self._end_point

    def set_end_point(self, point):
        self._end_point = point
        self._length = self.compute_length()

    def get_length(self):
        return self._length

    def compute_length(self):
        return self._start_point.compute_distance(self._end_point)
