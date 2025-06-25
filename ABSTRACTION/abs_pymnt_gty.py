from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def Pay(self,amount):
        pass

class creditcard(PaymentMethod):
    def Pay(self,amount):
        self.amount = amount
        print(f"Amount {self.amount} Paid by CreditCard")

class Upi(PaymentMethod):
    def Pay(self,amount):
        self.amount = amount
        print(f"Amount {self.amount} Paid by UPI")

class PayPal(PaymentMethod):
    def Pay(self,amount):
        self.amount=amount
        print(f"Amount {self.amount} Paid by PayPal")

c1=creditcard()
u1=Upi()
p1=PayPal()

for Method in (c1,u1,p1):
    Method.Pay(2000)