from abc import ABC,abstractmethod
class Loan(ABC):
    @abstractmethod
    def interest_cal(self,amount,time):
        pass

class HomeLoan(Loan):
    def interest_cal(self,amount,time):
        self.rate = 7.5
        print("\nPrinting Simple Interest:>>>\n")
        print("Home Loan Interest Calculation:")
        SI=(amount*time*self.rate)/100
        print(f"Your Interest is : {SI}")

class CarLoan(Loan):
    def interest_cal(self, amount, time):
        self.rate = 8
        print("Car Loan Interest Calculation:")
        SI = (amount * time * self.rate) / 100
        print(f"Your Interest is: {SI}")

class EducationLoan(Loan):
    def interest_cal(self, amount, time):
        self.rate = 4.5
        print("Education Loan Interest Calculation:")
        SI = (amount * time * self.rate) / 100
        print(f"Your Interest is: {SI}")

loans = [HomeLoan(), CarLoan(), EducationLoan()] # loop use krne se line of code kam hoga 

for loan in loans:
    loan.interest_cal(10000, 2)  # same amount and time for all 
    print("__________________________________________")

'''h1=HomeLoan()            Amount different for different loan 
h1.interest_cal(5000,2)'''