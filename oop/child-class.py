class Person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age

    def intro(self):
          print(self.name,self.surname,self.age)    


class student(Person):
        def __init__(self, name, surname, age,number):
              Person.__init__(self,name,surname,age)
              self.number=number
              print("student sınıfı türetildi")

class teacher(Person):
        pass
    
p1=Person("sadık","turan",40)
p1.intro()

s1=student("çınar","turan",7,2480)
s1.intro()

t1=teacher("çınar","turan",7)
t1.intro()