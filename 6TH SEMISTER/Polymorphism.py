class Animal:   #Parent Class
    def sound(self):
        print("Animal Sound")

class Dog(Animal):   # Child class 
    def sound(self):  # Method Overridding
        print("Dog Sound")



a = Animal()
a.sound()
d = Dog()
d.sound()

# Python does not support Method OverLoading