class vehicle:
    def __init__(self,brand, model, year):
        self.brand= brand
        self.model = model                              # Hierarchical Inheritance 
        self.year = year

class car(vehicle):
    def __init__(self,brand,model,year,fuel_type,no_of_doors):
        super().__init__(brand,model,year)
        self.fuel_type = fuel_type
        self.no_of_doors = no_of_doors

    def display_details(self):
        print(f"\n The car Brand is : {self.brand} \n The model is : {self.model} \n Manufacture Year is : {self.year}")
        print(f" The fuel type is : {self.fuel_type} \n The no of doors is : {self.no_of_doors}")
        print("________________________________")

class Truck(vehicle):
    def __init__(self,brand,model,year,load_capacity):
        super().__init__(brand,model,year)
        self.load_capacity = load_capacity

    def display_details(self):
        print(f"\n The Truck Brand is : {self.brand} \n The model is : {self.model} \n Manufacture Year is : {self.year}")
        print(f" The load_capacity is : {self.load_capacity} TON")
        print("________________________________")

class Bike(vehicle):
    def __init__(self,brand,model,year,is_geard):
        super().__init__(brand,model,year)
        self.is_geard = is_geard

    def display_details(self):
        print(f"\n The Bike Brand is : {self.brand} \n The model is : {self.model} \n Manufacture Year is : {self.year}")
        print(f" Is_geard : {self.is_geard} ")
        print("________________________________")

c1=car("Tyota","Defender",2021,"diesel",4)
t1=Truck("Leyland","Loader",2018,1000)
b1 = Bike("Yahama","r15",2025,"YES")


'''c1.display_details()
b1.display_details()
t1.display_details()'''


while True:
    print("\n1. For Car Details: ")
    print("2. For Truck Details: ")
    print("3. For Bike Details: ")
    print("4. For Exit: \n")
    print("________________________________")

    choice = input("Enter Your Choice: ")
    print("________________________________")
    if choice=="1":
        c1.display_details()
    elif choice=="2":
        t1.display_details()
    elif choice=="3":
        b1.display_details()
    elif choice=="4":
        print("Exiting..........")
        break
    else:
        print("Invalid choice!!!!!")

'''
for l in (c1,t1,b1):
    l.display_details()
    print("______________________________________________")'''