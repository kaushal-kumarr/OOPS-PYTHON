class object_counter:
    count = 0

    def __init__(self):
        object_counter.count+=1
    @classmethod
    def show_count(cls):
        print("The Total count is : ",object_counter.count)

obj1= object_counter()
obj2= object_counter()


object_counter.show_count()
