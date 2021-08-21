import math as m

class Shape:
    pass
class Polygon(Shape):
    def __init__(self, length):
        self.side_length = length
    def area(self):
        pass
    
class Triangle(Polygon):
    def __init__(self,length):
        super().__init__(length)
        self.sides = 3
    def area(self):
        return (m.sqrt(3)/4) * (self.side_length ** 2)

class Square(Polygon):
    def __init__(self,length):
        super().__init__(length)
        self.sides = 4
    def area(self):
        return self.side_length ** 2

class Pentagon(Polygon):
    def __init__(self,length):
        super().__init__(length)
        self.sides = 5
    def area(self):
        return 0.25 * (m.sqrt(5 * (5 + 2 * m.sqrt(5)))) * (self.side_length ** 2)

class Hexagon(Polygon):
    def __init__(self,length):
        super().__init__(length)
        self.sides = 6
    def area(self):
        return (3* m.sqrt(3))/2 * (self.side_length ** 2)
class Heptagon(Polygon):
    def __init__(self,length):
        super().__init__(length)
        self.sides = 7
    def area(self):
        return (7/4) * 1/(m.tan(m.pi/7)) * (self.side_length ** 2)

class Octagon(Polygon):
    def __init__(self,length):
        super().__init__(length)
        self.sides = 8
    def area(self):
        return 2 * (1 + m.sqrt(2)) * (self.side_length ** 2)



B = Octagon(3)
print(B.area())

