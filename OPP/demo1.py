class Student:
    def __init__(self):   # constructor
        self.name = 'Bappi'
        self.age = 21
        self.mark = 94
    def talk(self):
        print('hello i am :',self.name)
        print('my age is :', self.age)
        print('My mark is :',self.mark)

s=Student()
s.talk()



