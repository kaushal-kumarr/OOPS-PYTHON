from abc import ABC, abstractmethod

class SmartDevice(ABC):
    @abstractmethod                                     # Hierarchical Inheritance
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):             
        pass

class SmartLight(SmartDevice):
    def __init__(self, choice):
        self.choice = choice.lower()  

    def turn_on(self):
        if self.choice == "on":
            print("SmartLight Turned !ON!")
        elif self.choice == "off":
            self.turn_off()
        else:
            print("Invalid input! Please enter ON or OFF.")

    def turn_off(self):
        print("SmartLight Turned !OFF!")


class SmartAC(SmartDevice):
    def __init__(self, choice):
        self.choice = choice.lower()  

    def turn_on(self):
        if self.choice == "on":
            print("SmartAC Turned !ON!")
        elif self.choice == "off":
            self.turn_off()
        else:
            print("Invalid input! Please enter ON or OFF.")

    def turn_off(self):
        print("SmartAC Turned !OFF!")

choice = input("FOR SMARTLIGHT----> Enter choice !ON! or !OFF!: ").strip()
L1 = SmartLight(choice)
L1.turn_on()

choice = input("FOR SMARTAC----> Enter choice !ON! or !OFF!: ").strip()
A1 = SmartAC(choice)
A1.turn_on()

