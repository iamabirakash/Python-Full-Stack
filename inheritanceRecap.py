class Person:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Name :-",self.name)

class Student(Person):
    def __init__(self,name,rollno):
        super().__init__(name)
        self.rollno = rollno
    def show(self):
        self.display()
        print("Roll No :-",self.rollno)

p = Person("Anthony")
p.display()
s = Student("Akhil",22)
s.show()