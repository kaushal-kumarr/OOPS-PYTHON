from abc import ABC, abstractmethod
class Basecourse(ABC):
    @abstractmethod
    def enroll(self):
        pass
    @abstractmethod
    def get_material(self):
        pass
    @abstractmethod
    def submit_assg(self):
        pass

class course(Basecourse):
    def enroll(self):
        print("You Enrolled in the course ")
    def get_material(self):
        print("Study Material Coming Soon.....")
    def submit_assg(self):
        print("Assignment Submitted Succesfully.")

s1=course()

s1.enroll()
s1.get_material()
s1.submit_assg()