class Dog:
    def __init__(self,name,breed,age):
        self.name = name   # Public Instance Variable
        self._breed = breed  # Protected Instance Varible
        self.__age = age    # Private Instance Variable

    def get_age(self):
        return self.__age
    

d = Dog("Buddy","Labrador",10)

print(d.name, d._breed)
print(d.get_age()) 