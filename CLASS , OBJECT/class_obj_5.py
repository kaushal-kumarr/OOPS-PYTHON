class demo:
    a =5
    def __init__(self):
        pass

    def display(self):
        print(f"{self.a}")


obj = demo()
obj.a = 0

obj.display()
print(demo.a)