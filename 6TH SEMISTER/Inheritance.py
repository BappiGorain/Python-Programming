class Dog:
    def __init__(self,name):
        self.name = name
    
    def display(self):
        print(self.name)

class Labrador(Dog):     # Single Inheritance
    def sound(self):
        print(self.name,"Labrador woofs")

class GuideDog(Labrador):   # Multilevel Inheritance
    def guide(self):
        print(self.name,self.sound,"GuideDog")



lab = Labrador("Buddy")
lab.display()
lab.sound()

gd  = GuideDog("Charlie")
gd.display()
gd.sound()
gd.guide()
