from abc import ABC, abstractmethod
class SmartClass(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class SmartFan(SmartClass):
    def turn_on(self):
        print("Your fan turned ON")
    def turn_off(self):
        print("Your fan turned OFF")

class SmartLight(SmartClass):
    def turn_on(self):
        print("Your light turned ON")
    def turn_off(self):
        print("Your light turned OFF")

class SmartAC(SmartClass):
    def turn_on(self):
        print("Your AC turned ON")
    def turn_off(self):
        print("Your AC turned OFF")

f1 = SmartFan()
l1 =SmartLight()
a1=SmartAC()

f1.turn_on()
l1.turn_on()
a1.turn_off()