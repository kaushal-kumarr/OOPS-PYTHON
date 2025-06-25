class complex:
    def __init__(self,real,img):
        self.real = real
        self.img=img

    def show (self):
        print(f"{self.real} i + {self.img} j")

    def __add__(self,num2):
        newReal = self.real+num2.real
        newImg = self.img+num2.img
        print(f"{newReal} i + {newImg} j")

num1 = complex(3,4)
num1.show()
num2 = complex(5,2)
num2.show()
print("_____________")
num1.__add__(num2)