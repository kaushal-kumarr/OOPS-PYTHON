class DataConnector:
    def __init__(self, db_user, db_password, token):
        self.__db_user = db_user                            # SHOWING ENCAPSULATION 
        self.__db_password = db_password                    # MAKING PRIVATE 
        self.__token = token 

    def connect(self, token):
        if token == self.__token:
            print(f"Connection successful as user: {self.__db_user}")
        else:
            print("Access Denied: Invalid token.")

    def update_credentials(self, user, password, token):
        if token == self.__token:
            self.__db_user = user
            self.__db_password = password
            print("Credentials updated successfully.")
        else:
            print("Invalid token. Cannot update credentials.")

    def get_credentials(self, admin=False):
        if admin:
            return {
                "user": self.__db_user,
                "password": self.__db_password
            }
        else:
            masked_pass = "*" * len(self.__db_password)
            return {
                "user": self.__db_user,
                "password": masked_pass
            }

connector = DataConnector("kaushal", "Kumar@123", "k001")

connector.connect("k101")  # token match nhi hoga too connect nhi hoga 
connector.connect("k001")      

print(connector.get_credentials())  # credential to dekhne ke liye hm direct nhi dekh skte hai isiiliye function banana pada hai, private ke wajh se 

print(connector.get_credentials(admin=False))  

connector.update_credentials("Raunak", "Raunak123", "wrong_token") # token wrong hai to update nhi hoga  
connector.update_credentials("Raunak", "Raunak123", "k001") 

'''Base class me koi v value ko update krne ke liye hm direct nhi kr skte hai kyuki sab 
private hai issiliye function bana ke update krna hoga aur function base class 
me hi hona chahiye'''

print(connector.get_credentials(admin=True))  
