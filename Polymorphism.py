#Inheritance--> reusability
#polymorphism-->same function, but different behaviour
#encapsulation--> data security
#Abstraction--> access control, hiding the implementation part, to hide unneccessary info
#constructor overloading--> same name but diff parameters
#overloading--> we are changing the parameters
#overriding--> same function name, but different definition
class vehicle:
    def __init__(self,model,color):
        self.model=model;
        self.color=color;
    def display(self):
        print(f"Model: {self.model} and color is: {self.color}")
class Car(vehicle):
    #Constructor overloading
    def __init__(self,model,color,seats):
        super().__init__(model,color)
        self.seats=seats
    #method overriding
    def display(self):
        super().display();
        print("seats are ", self.seats);
obj=vehicle("BMW","Black");
obj.display();
obj2= Car("Creta","White",5)
obj2.display();
#this program is an example of polymorphism --> same function but different behaviour

#polymorphism--> method can behave different, diff behaviour in both classes
#super+overriding --> runtime polymorphism

#Encapsulation--> binding the data
#Access modifiers--> public, private--> access only from inside the class, protected--> we can only access them by inheriting

# class Employee:
#     def __init__(self):
#         self.name="Emply";#public
#         self.__id=1;#private
#     def getId(self): #getter method --> to get the private id
#         return self.__id;
#     def setId(self,value): #setter method--> to updat ethe private variable
#         self.__id=value;
# obj=Employee();
# print(obj.name);
# print(obj.__id)  #--> __(double _ --> private), _(single _ --> protected)
# obj.__=2;  #this will not run bcz pf private variable we need to use setter for this to access this
# print(obj.getId());
#private--> neither update nor access
# obj.setId(3)
# print(obj.getId())

# class Student:
#     def __init__(self):
#         self.__name="ABC";
#         self.__age=12;
#         self.__marks=89;
#     def getId(self):
#         return self.__name,self.__age,self.__marks;
#     def setId(self,Name, Age, Marks):
#         self.__name=Name;
#         self.__age=Age;
#         self.__marks=Marks;
# obj=Student();
# print(obj.getId());
# obj.setId("XYZ",17,98)
# print(obj.getId());
    
#it will be difficult for us to make getter and setter for each variable --> so instead of this we cqn use property decorators
#we use property decorators--> easy to access, easy to store, easy to implement or read, 
# class Studnet:
#     def __init__(self,marks):
#         self.marks=marks; #private variable

#     @property
#     def marks(self):  #getter
#         return self.__marks;
#     @marks.setter
#     def marks(self,value):  #setter
#         self.__marks=value;

# s1=Studnet(80);
# s1.marks=90
# print(s1.marks)

# we can achieve encapsulation using access modifiers

#Abstraction--> Hding the implementations or showing essentiall details
#Security
#setting some rules
#Abstract class= Always Act like a base class,it can have both abstract and non abstract method
#Abstract method-->  jino parent class mai empty rkhte hai and further child class mai ovveride krke access krte hai
#non-abstract method--> non-empty, whose logic already written in parent class
#Abstract method--> empty methods which will be updated in child class

from abc import ABC, abstractmethod
# class Employee(ABC):  #Abstract class, this is a bse class of ABC
#     @abstractmethod
#     def greet(self):#we are hiding the implementaion of the greek method
#         pass; #this is Abstarct method, empty method
#     def hello(self):
#         print("Hello.......")#Non-Abstarct method
# class Technical(Employee):
#     def greet(self):
#         print("Hii, i am an employee from it dept.....");

# obj=Technical();
# obj.greet();
# obj.hello();

# class ATM:
#     @abstractmethod
#     def withdraw(self,amount):
#         pass;
# class SBI:
#     def withdraw(self,amount):
#         print("Acessing bank acc.....")
#         print("Amount withdraw: ", amount)
# atm=SBI();
# atm.withdraw(50000)

#exception handling: to maintain the flow of our program
class AgeNotValid(Exception):
    pass;
class Person:
    def __init__(self,age):
        if(age<18):
            raise AgeNotValid("Age should not below than 18");
        self.age=age;
try:      #code in which we feel that maybe an error will occur
    obj=Person(17);
    # obj=Person(20);
    print(obj.age);
except AgeNotValid as e:   #if any code occurinside try block it will come to the except block
    print(e)

