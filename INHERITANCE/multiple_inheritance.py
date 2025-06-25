                # Smart Vehicle Control System

class ElectricVehicle:
    def run(self):                      #  MULTIPLE INHERITANCE
        print("Charging ||| Battery ")

class AutonomousVehicle:
    def sensor(self):
        print("It can Navigate And Park Easily ")

class EntertainmentSystem:
    def music(self):
        print("It has inbuilt music system with voice command ")

class TeslaModel(ElectricVehicle,AutonomousVehicle,EntertainmentSystem):
     def features(self):
        print("\nTesla Model Features Overview:\n")
        self.run()
        self.sensor()
        self.music()

my_tesla = TeslaModel()
my_tesla.features()

El =ElectricVehicle()
print("\n FOR ELECTRIC VEHICLE")
El.run()
