class Student:
    def __init__(self,name,age,mark): 
        self.name = name
        self.age = age
        self.mark = mark
    def talk(self):
        print('hello i am :',self.name)
        print('my age is :', self.age)
        print('My mark is :',self.mark)

s1=Student('Bappi',21,94)
s1.talk()
s2=Student('Gopi',18,90)
s2.talk()


    
