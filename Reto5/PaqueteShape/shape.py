from .line import Line

class Shape:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = self.compute_edges()
        self._inner_angles = []
        self._is_regular = False

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, vertices):
        self._vertices = vertices
        self._edges = self.compute_edges()

    def get_edges(self):
        return self._edges

    def get_inner_angles(self):
        return self._inner_angles

    def set_inner_angles(self, inner_angles):
        self._inner_angles = inner_angles

    def get_is_regular(self):
        return self._is_regular

    def set_is_regular(self, is_regular):
        self._is_regular = is_regular

    def compute_area(self):
        pass

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self._edges)

    def compute_edges(self):
        edges = []
        for i in range(len(self._vertices)):
            start_point = self._vertices[i]
            end_point = self._vertices[(i + 1) % len(self._vertices)]
            edges.append(Line(start_point, end_point))
        return edges
