class counter:
    def __init__(self):
        self.count =0

    def increament(self):
        self.count+=1
        print(f"counter increamented : {self.count}")
    def decreament(self):
        self.count-=1
        print(f"counter decreamented : {self.count}")

    def reset(self):
        self.count=0
        print(f"counter reset: {self.count}")
    def get_value(self):
        print("Value is: ",self.count)

c1=counter()
c1.increament()
c1.increament()
c1.increament()

c1.decreament()
c1.get_value()
c1.reset()
c1.get_value()
