from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def rent(self):
        pass

class bike(vehicle):
    def start(self):
        print("The Bike has Started..")
    def stop(self):
        print("The Bike has Stopped..")
    def rent(self):
        print("The Bike is on rent at Rs. 500 per day")

class car(vehicle):
    def start(self):
        print("The car has Started..")
    def stop(self):
        print("The car has Stopped..")
    def rent(self):
        print("The car is on rent at Rs. 1500 per day")

class truck(vehicle):
    def start(self):
        print("The Truck has Started..")
    def stop(self):
        print("The Truck has Stopped..")
    def rent(self):
        print("The Truck is on rent at Rs. 500 per day")

b1 = bike()
c1 = car()
t1 = truck()

for vehicle in (b1,c1,t1):
    vehicle.start()
    vehicle.stop()
    vehicle.rent()
    print("___________________________________")