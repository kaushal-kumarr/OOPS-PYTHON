from abc import ABC, abstractmethod
class food_delivery(ABC):
    @abstractmethod
    def deliver_order(self):
        pass

class zomato(food_delivery):
    def deliver_order(self):
        print("It can deliver order in 30 minutes by bike")

class swiggy(food_delivery):
    def deliver_order(self):
        print("It can deliver order in 20 minutes by bike and drown")

class ubereats(food_delivery):
    def deliver_order(self):
        print("It can deliver order in 25 minutes by bike and car")

z1=zomato()
z1.deliver_order()
s1 =swiggy()
s1.deliver_order()
u1=ubereats()
u1.deliver_order()