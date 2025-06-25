class programmer:
    company = "Microsoft"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f" Your Name is {self.name}\n Your company is : {self.company}\n Your salary is: {self.salary}")
        
e1=programmer("Kaushal",25000)
e2=programmer("rahul",32000)

e1.display()
e2.display()