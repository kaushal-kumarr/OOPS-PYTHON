            # Hospital Staff Scheduling System

class Doctor:
    def diagnose(self):                      #  MULTIPLE INHERITANCE
        print("Diagnose Disease")

class Researcher:
    def publish_paper(self):
        print("He publish paper ")

class Admin_Staff:
    def manage_schedule(self):
        print("He manages all schedule ")

class MedicalDirector (Doctor,Researcher,Admin_Staff):
     def features(self):
        print("\nMedicalDirector Handles :\n")
        self.diagnose()
        self.publish_paper()
        self.manage_schedule()

d1=Doctor()
d1.diagnose()

r1 = Researcher()
r1.publish_paper()

a1 =Admin_Staff()
a1.manage_schedule()


M1 = MedicalDirector ()
M1.features()