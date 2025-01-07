from PaqueteShape import Point, Line, Shape, Rectangle, Square

def main():


# Crear puntos
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 3)
    p4 = Point(0, 3)

# Crear una línea entre dos puntos
    line = Line(p1, p2)
    print("Longitud de la línea:", line.get_length())

# Crear una forma genérica (un cuadrilátero en este caso)
    vertices = [p1, p2, p3, p4]
    shape = Shape(vertices)
    print("Perímetro de la forma genérica:", shape.compute_perimeter())

# Crear un rectángulo
    rectangle = Rectangle(4, 3)
    print("Área del rectángulo:", rectangle.compute_area())
    print("Perímetro del rectángulo:", rectangle.compute_perimeter())

# Crear un cuadrado
    square = Square(5)
    print("Área del cuadrado:", square.compute_area())
    print("Perímetro del cuadrado:", square.compute_perimeter())

    
if __name__ == "__main__":
    main()
