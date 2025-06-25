class calculator:
    def __init__(self,number):
        self.number = number

    def square(self):
        print(f"The square of {self.number} is {self.number*self.number}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number*self.number*self.number}")

    def square_root(self):
        print(f"The square root of {self.number} is {self.number**(1/2)}")


number = int(input("Enter the Number : "))

n1= calculator(number)
n1.square()
n1.cube()
n1.square_root()