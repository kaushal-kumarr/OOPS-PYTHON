from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def Draw(self):
        pass
    @abstractmethod
    def Calculate_area(self):
        pass

class Circle(shape):
    def __init__(self,radius):
       self.radius=radius

    def Draw(self):
        print("Drawing a Circle:...")
    def Calculate_area(self):
        print(f"The Area of Circle is : {3.14*self.radius*self.radius}")

class Rectangle(shape):
    def __init__(self,length,breadth):
       self.length=length
       self.breadth=breadth

    def Draw(self):
        print("Drawing a Rectangle:...")
    def Calculate_area(self):
        print(f"The Area of Rectangle is : {self.length*self.breadth}")

class Triangle(shape):
    def __init__(self,base,height):
       self.base=base
       self.height=height

    def Draw(self):
        print("Drawing a Triangle:...")
    def Calculate_area(self):
        print(f"The Area of Triangle is : {(self.base*self.height)/2}")

c1=Circle(5)
r1=Rectangle(5,4)
t1=Triangle(2,8)

for ar in (c1,r1,t1):
    ar.Draw()
    ar.Calculate_area()
    print("______________________________")