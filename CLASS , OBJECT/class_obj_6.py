
import random
class Train :
    def __init__(self,train_no,fro,to):
        self.train_no = train_no
        self.fro=fro
        self.to =to
    def book_ticket(self):
        print(f"Your train number is {self.train_no}  You booked tkt from {self.fro} to {self.to}")

    def get_status(self):
        print( f"Your train having no.. {self.train_no} is running on time ")

    def get_fare(self):
        print("Your total fare is :",random.randint(300,2500))

train_no = int(input("Enter Train Number : "))
From = input("Station From : ")
To= input("Station To : ")
p1 =Train(train_no,From,To)
while True:
    print("\n======== Indian Railways ========")
    print("1. Book Ticket")
    print("2. Get Train Status")
    print("3. Get Fare Info")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        p1.book_ticket()
    elif choice == '2':
       p1.get_status()
    elif choice == '3':
        p1.get_fare()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")


