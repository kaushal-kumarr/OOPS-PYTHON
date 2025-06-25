from abc import ABC,abstractmethod
class User(ABC):
    @abstractmethod
    def get_discounted_price(self):
        pass

class GuestUser(User):
    def get_discounted_price(self,amount):
        self.amount = amount
        print("You have no discount....")
        print(f"Your Price is: {self.amount}")
        print("__________________________________________________________")
class RegularUser(User):
    def get_discounted_price(self,amount):
        self.amount = amount
        discount = amount/10
        print(f"Your Original Price is {self.amount} \nYou have 10% discount {discount} \nYour Final Price is : {self.amount-discount}")
        print("__________________________________________________________")

class PremiumUser(User):
    def get_discounted_price(self,amount):
        self.amount = amount
        discount = amount/5
        print(f"Your Original Price is {self.amount} \nYou have 20% discount {discount} \nYour Final Price is : {self.amount-discount}")
        print("__________________________________________________________")

while True:
    print("1. For Guest User >>>>>>")
    print("2. For Regular User >>>>>>")
    print("3. For Premium User >>>>>>")
    print("4. Exit...")

    choice=input("Enter your Choice>>")

    if choice=="1":
        money = int(input("Enter Amount >> "))
        g1=GuestUser()
        g1.get_discounted_price(money)

    elif choice=="2":
        money = int(input("Enter Amount >> "))
        r1=RegularUser()
        r1.get_discounted_price(money)
    elif choice=="3":
        money = int(input("Enter Amount >> "))
        p1=PremiumUser()
        p1.get_discounted_price(money)
    elif choice=="4":
        break
    else:
        print("Invalid choice.!!!!!!!!")