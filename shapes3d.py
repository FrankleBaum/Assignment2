import math
import Shapes

#Cuboid Definition (rectangular prism)
class Cuboid:
    def __init__(self, width:float, height:float, depth:float):
        self.width = width
        self.height = height
        self.depth = depth

    def getArea(self):
        return 2 * ((self.width * self.height) + (self.width * self.depth) + (self.height * self.depth))

    def getVolume(self):
        return (self.width) * (self.height) * (self.depth)

#Cube Definition (square prism)
class Cube:
    def __init__(self, side:float):
        self.width = side
        self.height = side
        self.depth = side

    def getArea(self):
        return 2 * ((self.width * self.height) + (self.width * self.depth) + (self.height * self.depth))

    def getVolume(self):
        return (self.width) * (self.height) * (self.depth)

#Cylinder Definition
class Cylinder:
    def __init__(self, radius:float, height:float):
        self.radius = radius
        self.height = height

    def getArea(self):
        return ((2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius ** 2))
    
    def getVolume(self):
        return math.pi * self.radius **2 * self.height
        
#Sphere Definition
class Sphere:
    def __init__(self, radius:float):
        self.radius = radius

    def getArea(self) -> float:
            return 4 * math.pi * (self.radius ** 2)

    def getVolume(self) -> float:
            return (4/3) * math.pi * (self.radius ** 3)

#Prism Definition
class Prism:
    def __init__ (self, sideLength, sides, height):
        self.base = Shapes.Polygon(sideLength, sides).GetArea()
        self.perimeter = Shapes.Polygon(sideLength, sides).GetPerimeter()
        self.height = height

    def getArea(self):
        return (2 * self.base) + (self.perimeter * self.height)
    
    def getVolume(self):
        return self.base * self.height