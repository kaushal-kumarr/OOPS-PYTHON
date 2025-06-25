from abc import ABC, abstractmethod

class DatabaseConnector(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self):
        pass

class MySQLConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")

    def __init__(self,query):
        self.query=query

    def execute_query(self):
        print(f"Executing MySQL query: {self.query}")

class PostgreSQLConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")
    def __init__(self,query):
        self.query=query

    def execute_query(self):
        print(f"Executing PostgreSQL query: {self.query}")

class MongoDBConnector(DatabaseConnector):
    def connect(self):
        print("Connecting to MongoDB database...")

    def disconnect(self):
        print("Disconnecting from MongoDB database...")

    def __init__(self,query):
        self.query=query

    def execute_query(self):
        print(f"Executing MongoDB query: {self.query}")


sql1=MySQLConnector("SELECT * FROM users")
Psql1=PostgreSQLConnector("SELECT * FROM employees")
Mondb1=MongoDBConnector("find: 'products")

for ex in (sql1,Psql1,Mondb1):
    ex.connect()
    ex.execute_query()
    ex.disconnect()
    print("__________________________________________")