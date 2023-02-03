import shapes3d
import csv
class Solver:
    def __init__(self , fileName):
        self.Shapes = [] #This is an empty Shapes array
        self.total = 0 #This is a running total
        
        with open(fileName , mode ='r')as file:
            csvFile = csv.reader(file, delimiter=',')
            for line in csvFile:
                if line[0] == "cuboid":
                    #appending shape to Shapes array
                    self.Shapes.append(shapes3d.Cuboid(float(line[1]), float(line[2]), float(line[3])))
                elif line[0] == "cube":
                    self.Shapes.append(shapes3d.Cube(float(line[1])))
                elif line[0] == "sphere":
                    self.Shapes.append(shapes3d.Sphere(float(line[1])))
                elif line[0] == "cylinder":
                    self.Shapes.append(shapes3d.Cylinder(float(line[1]), float(line[2])))
                elif line[0] == "prism":
                    self.Shapes.append(shapes3d.Prism(float(line[1]), float(line[2]), float(line[3])))
                elif line[0] == "area":
                    for shape in self.Shapes:
                        self.total += shape.getArea() * float(line[1])
                    self.Shapes = [] #this empties the Shapes array
                elif line[0] == "volume":
                    for shape in self.Shapes:
                        self.total += shape.getVolume() * float(line[1])
                    self.Shapes = [] #this empties the Shapes array

if __name__ == "__main__":
    solver = Solver("TestValues.csv") #creating solver object 
print("The total of measurements requested is {:,.2f}".format(solver.total)) #printing total returned by solver and formating return value