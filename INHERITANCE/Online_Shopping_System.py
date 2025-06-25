from abc import ABC, abstractmethod
class user(ABC):
    def __init__(self,name,email):                          # Hierarchical Inheritance
        self.name = name
        self.email = email
    @abstractmethod
    def get_role(self):
        pass

class customer(user):
    def __init__(self, name, email):
        super().__init__(name, email)

    def place_order(self):
        print("You can place order..")

    def get_role(self):
        print(f"{self.name} is a customer ")

class seller(user):
    def __init__(self, name, email):
        super().__init__(name, email)

    def add_product(self):
        print("You can add product..")

    def get_role(self):
        print(f"{self.name} is a seller ")

class admin(user):
    def __init__(self, name, email):
        super().__init__(name, email)

    def view_all_user(self):
        print("You can view all user..")

    def delete_user(self):
        print("You can delete user..")

    def get_role(self):
        print(f"{self.name} is an admin ")


c1=customer("rajesh","raj4586@gmail.com")
s1=seller("Kundan","kundan453@gmail.com")
a1=admin("Tarun","tarunn4586@gmail.com")

c1.place_order()
c1.get_role()
s1.add_product()
s1.get_role()
a1.view_all_user()
a1.delete_user()
a1.get_role()