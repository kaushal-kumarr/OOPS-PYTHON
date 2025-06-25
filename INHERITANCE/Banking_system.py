class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name                        # Hierarchical Inheritance
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print(" Deposit amount must be positive!")
        else:
            self.balance += amount
            print(f" ₹{amount}deposited-----> New Balance: ₹{self.balance}")
        print("____________________________________________")

    def withdraw(self, amount):
        if amount <= 0:
            print(" Withdraw amount must be positive!")
        elif amount > self.balance:
            print(f" Insufficient balance to withdraw ₹{amount}")
        else:
            self.balance -= amount
            print(f" ₹{amount}withdrawn-----> New Balance: ₹{self.balance}")
        print("____________________________________________")

    def get_balance(self):
        print(f" Your Balance is: ₹{self.balance}")
        print("____________________________________________")


class saving_acc(BankAccount):
    def __init__(self, acc_no, name, balance):
        print("\nFOR SAVING ACCOUNT")
        super().__init__(acc_no, name, balance)
        self.withdraw_count = 0
        self.max_withdraw_count = 4

    def withdraw(self, amount):
        if self.withdraw_count >= self.max_withdraw_count:
            print(" Maximum withdrawal limit (4) reached.")
        else:
            super().withdraw(amount)
            self.withdraw_count += 1


class current_acc(BankAccount):
    def __init__(self, acc_no, name, balance):
        print("\nFOR CURRENT ACCOUNT")
        super().__init__(acc_no, name, balance)
        self.min_balance = 1000

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print(f" Cannot withdraw ₹{amount}. Minimum balance ₹{self.min_balance} must be maintained.")
            print("____________________________________________")
        else:
            super().withdraw(amount)


class salary_acc(BankAccount):
    def __init__(self, acc_no, name, balance, fixed_salary):
        print("\nFOR SALARY ACCOUNT")
        super().__init__(acc_no, name, balance)
        self.fixed_salary = fixed_salary

    def deposit(self):
        self.balance += self.fixed_salary
        print(f"Fixed salary ₹{self.fixed_salary} deposited.\nNew Balance: ₹{self.balance}")
        print("____________________________________________")

# Saving Account
sav = saving_acc(12345, "Kaushal", 2000)
sav.deposit(3000)
sav.withdraw(500)
sav.withdraw(-500)
sav.withdraw(500)
sav.withdraw(500)  
sav.get_balance()

# Current Account
curr = current_acc(23456, "Rahul", 5000)
curr.deposit(1000)
curr.withdraw(4500)  
curr.withdraw(3000)  
curr.get_balance()

# Salary Account
sal = salary_acc(34567, "Ankit", 1000, 20000)
sal.deposit()
sal.withdraw(5000)
sal.get_balance()
