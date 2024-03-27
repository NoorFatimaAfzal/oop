class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*(radius**2)
    def perimeter(self):
        return 2*3.14*radius

radius=int(input("Enter radius: "))
circle1=circle(radius)
print(circle1.area())