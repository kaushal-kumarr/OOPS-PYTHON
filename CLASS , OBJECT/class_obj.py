class student:          # defining a class 
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    @staticmethod           # iske likhne se greet function object pe depend nhi rhega 
    def greet():
        print("Good Morning!")

    def display_details(self):
        print(f"Hello {self.name} Your Roll No is : {self.roll_no}")

s1=student("Kaushal",1)
s2 = student("rahul",2)
s1.greet()          # isko ham student.greet() krke v call kr skte hai 
s1.display_details()
s2.display_details()

