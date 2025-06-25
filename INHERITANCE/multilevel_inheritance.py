
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.department = department

    def show_employee_info(self):
        self.show_person_info()
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")

class Manager(Employee):
    def __init__(self, name, age, emp_id, department, team_size, bonus):
        super().__init__(name, age, emp_id, department)
        self.team_size = team_size
        self.bonus = bonus

    def show_manager_info(self):
        self.show_employee_info()
        print(f"Team Size : {self.team_size}")
        print(f"Bonus: ₹{self.bonus}")

m1 = Manager("Kaushal Singh", 24, "E1023", "Technology", 5, 25000)

m1.show_manager_info()
