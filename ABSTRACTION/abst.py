class car :
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False
    def car_start(self):
        self.acc=True
        self.clutch=True
        print("Car has Started....")

c1=car()

c1.car_start()