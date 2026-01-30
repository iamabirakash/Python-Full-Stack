# class Vehicle:
#     def show(self):
#         print("This is Vehicle")
# class Car(Vehicle):
#     def info(self):
#         print("This is Car")
# class EV(Car):
#     def display(self):
#         print("This is an EV Car")

# ev = EV()
# ev.show()
# ev.info()
# ev.display()

class Person:
    def __init__(self,name,regno):
        self.name = name
        self.__regno = regno
    def show(self):
        print("Name :-",self.name)
        print("Regno :-",self.__regno)
class Employee(Person):
    def __init__(self,name,regno,sal,empid):
        super().__init__(name,regno)
        self.sal = sal
        self._empid = empid
    def info(self):
        print("Salary :-",self.sal)
        print("Emp ID :-",self._empid)
class Manager(Employee):
    def __init__(self, name, regno, sal, empid, dept):
        super().__init__(name, regno, sal, dept)
        self.dept = dept
    def display(self):
        print("Department :-",self.dept)
m = Manager("Abir", "21CSE001", 1000000, "EMP101", "CSE")
m.display()
m.info()
m.show()
print("---------")
print(m.name)
print(m._empid)