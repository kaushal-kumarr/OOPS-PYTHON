class employee:
    def __init__(self,name, emp_id,base_salary):
        self.name=name
        self.emp_id=emp_id                              # Hierarchical Inheritance
        self.base_salary=base_salary
    
class fulltime(employee):
    def __init__(self, name, emp_id, base_salary,fixed_salary):
        super().__init__(name, emp_id, base_salary)
        self.fixed_salary=fixed_salary
    
    def display_details(self):
        print(f"\n Your Name is : {self.name}\n Your emp_id is : {self.emp_id} \n Your Base salary is : {self.base_salary}")

    def calculate_salary(self):
        print(f" Your Fixed Salary {self.fixed_salary} \n")

class part_time(employee):
    def __init__(self, name, emp_id,hourly_rate,hours):
        super().__init__(name, emp_id, 0)  # here i don't want to have base salry of part_time emp
        self.hourly_rate =hourly_rate
        self.hours=hours

    def display_details(self):
        print(f" Your Name is : {self.name}\n Your emp_id is : {self.emp_id} \n Your Base salary is : {self.base_salary}")

    def calculate_salary(self):
        print(f" Your Final Salary {self.hourly_rate*self.hours}\n")

class Intern (employee):
    def __init__(self, name, emp_id,Fix_stipend):
        super().__init__(name, emp_id, 0)
        self.fix_stipend =Fix_stipend

    def display_details(self):
        print(f" Your Name is : {self.name}\n Your emp_id is : {self.emp_id} \n Your Base salary is : {self.base_salary}")

    def calculate_salary(self):
        print(f" Your Final Salary{self.fix_stipend}\n")


f1=fulltime("Kaushal",101,15000,20000)
p1=part_time("Rahul",102,500,8)
i1=Intern("raunak",103,8000)

f1.display_details()
f1.calculate_salary()
p1.display_details()
p1.calculate_salary()
i1.display_details()
i1.calculate_salary()