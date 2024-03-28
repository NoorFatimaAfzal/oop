import math
class shape:
    def __init__(self):
        print("This is class of Shape! ")

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self,radius):
        return math.pi * (radius**2)
    def perimeter(self,radius):
        return 2 * math.pi * radius

class triangle(shape):
    def __init__(self,base,hight,side1,side2,side3):
        self.base=base
        self.hight=hight
        self.side1=side1
        self.side1=side2
        self.side1=side3
    def area(self):
        return (0.5 * self.base * self.hight)
    def perimeter(self):
        return self.side1+self.side2+self.side3
    
triangle1=triangle(20,30,1,2,3)
print(triangle1.area())

