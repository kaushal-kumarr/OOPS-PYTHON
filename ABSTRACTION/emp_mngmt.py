from abc import ABC, abstractmethod
class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTime(employee):
    def __init__(self,salary):
        self.salary = salary
    def calculate_salary(self):
        print(f"The FullTime Salary is:{self.salary}")
class PartTime(employee):       
    def __init__(self,hourly_rate,hours):
        self.hourly_rate=hourly_rate
        self.hours=hours
    def calculate_salary(self):
        print(f"The salary according to hour is: {self.hourly_rate*self.hours}")
f1=FullTime(30000)
p1=PartTime(200,8)

for salary in (f1,p1):
    salary.calculate_salary()