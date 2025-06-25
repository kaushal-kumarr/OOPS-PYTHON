class student:
    def __init__(self,name, marks):
        self.name=name
        self.marks = marks
    @staticmethod    
    def greet():
        print("Hii There!!!!!!")
    
    def get_avg(self):
        sum =0
        for i in self.marks:
            sum+=i
        print(f"Hiii  {self.name} Your average score is: {sum/3}")

s1 = student("Kaushal",[98,52,65])
s1.greet()
s1.get_avg()