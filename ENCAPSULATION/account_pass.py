class account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def get_pass(self):
        return self.__acc_pass

a1 = account("12345","abcde")

print(f"Account No is : {a1.acc_no}")
#print(f"Account No is : {a1.__acc_pass}")  # we can't directly access the password 

print(f"Account Pass is : {a1.get_pass()}") 


''' To access the password we must make a function inside the class ,
    beacuse inside class any function can access the private attribute'''