import math as m

class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def area(self):
        self.area = m.pi * self.radius

    def toString(self):
        return "(centre = "+ str(self.centre) + " ,  radius = " + str(self.radius) + " area = " + str(self.area) + " )"

    def __init__(self,centre,radius):
        self.centre = centre
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def toString(self):
        return "Centre at " + self.centre.toString() + ", radius=" + str(self.radius)

c = Circle(10,10)

print(c.toString())

c = Circle(10,5)

print(c.toString())

