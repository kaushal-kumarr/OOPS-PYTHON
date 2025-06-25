from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def move(self):
        pass

class dog(Animal):
    def make_sound(self):
        print("Dog Barks... BOW!! BOW !!")
    def move(self):
        print("Dog can Move and Run.")
    def type(self):         # child class me aur extra method add ho skta hai 
        print("omnivore ")

class cat(Animal):
    def make_sound(self):
        print("Cat Meows... Meow!! Meow!!")
    def move(self):
        print("Cat can Move and Run.")

d1 = dog()
c1 =cat()

d1.make_sound()
d1.move()
d1.type()
print("__________________________")
c1.make_sound()
c1.move()