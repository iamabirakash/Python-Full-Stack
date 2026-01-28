# why we need oops concept in python
# OOPS--> re-usability --> DRY
# Code Structure
# Real World Implementation
# Security  --> Encapsulation--> Wrap up the data; , Inheritance

#Class--> Blueprint for creating objects
#Objects--> instance of class

#Creating a class
# class Student:
#     #Attributes
#     id=" ";
#     name=" ";

#     #Methods
#     def show(self):
#         print("ID is: ", self.id)  #self refers to the current object
#         print("Name is: ",self.name)

# s1=Student(); #object created
# s1.id=2;
# s1.name="ABC";
# s1.show();
    #methods, calss variables and instance variables

# class Parents:
#     name=" ";
#     age=" "; #object

#     def show(self):
#         print("Name is: ",self.name)
#         print("Age is: ", self.age)
# p1=Parents();
# p1.name="Raman";
# p1.age=50;
# p1.show();

# p2=Parents();
# p2.name="Meena";
# p2.age=45;
# p2.show();

# class Employee:
#     name=" ";
#     age=" ";
#     id=" ";
#     salary=" ";
#     jobrole=" ";

#     def get_details(self):
#         print("Name is: ",self.name);
#         print("Age is: ", self.age);
#         print("Id is: ",self.id);
#         print("Salary is: ", self.salary)
#         print("Job Role is: ",self.jobrole);

# e1=Employee();
# e1.name="abc";
# e1.age=26;
# e1.id=9;
# e1.salary=70000;
# e1.jobrole="Big Data Engineer";
# e1.get_details()

# e2=Employee();
# e2.name="xyz";
# e2.age=23;
# e2.id=5;
# e2.salary=80000;
# e2.jobrole="Data Scientist";
# e2.get_details()

# class Employee:
#     Company="Google" #class vraible--> variable hich belong to only a class, same value
#     def seeDetails(self,id,name):
#         self.name=name; #instance variable--> belong to object and for every object its values be different
#         self.id=id;
#     def showDetials(self):
#         print(f"Name is: {self.name} and id is: {self.id} --> {self.Company}")
# e1=Employee();
# e1.seeDetails(1,"ABC");
# e1.showDetials()

# class Bank:
#     name=" ";
#     age=" ";
#     id=" ";
#     currentAmount=0;
#     def get_Details(self):
#         print("Customer Name: ",self.name)
#         print("Customer age: ",self.age)
#         print("Customer ID: ", self.id)
#     def withdraw(self, amount):
#         print("Remaining Amount: ",self.currentAmount-amount);
#         self.currentAmount=self.currentAmount-amount;
#     def deposit(self, depositAmount):
#         print("Deposit Amount: ", self.currentAmount+depositAmount);
#         self.currentAmount=self.currentAmount+depositAmount;
# b1=Bank();
# b1.name="xyz";
# b1.age=23;
# b1.id=5;
# b1.get_Details();
# b1.deposit(200000);
# b1.withdraw(50000);

# class Student:
#     college="LPU" #class variable
#     def details(self, name, id):
#         self.name=name;
#         self.id=id;
#     def show(self):
#         print(f"College is: {self.college} and name is: {self.name} and ID is: {self.id}")
# s1=Student();
# s1.details("XYZ",3);
# s1.show();


#Constructor-->__init__
#no return type
#like a function but there is no return type of this, and here we only assign the values to the variables
#in python we make constructor using init, n but in cpp constructor is made up of class name
#in constructor we have to give attribute
# updated automatically during object creation
# class Student:
#     college="LPU" #class variable
#     def __init__(self,name):
#         self.name=name;
# s1=Student("Labesh");
# print(s1.name);


# class Bank:
#     name=" ";
#     age=" ";
#     id=" ";
#     currentAmount=0;
#     def __init__(self, name, age, id):
#         self.name=name
#         self.age=age
#         self.id=id
#     def withdraw(self, amount):
#         print("Remaining Amount: ",self.currentAmount-amount);
#         self.currentAmount=self.currentAmount-amount;
#     def deposit(self, depositAmount):
#         print("Deposit Amount: ", self.currentAmount+depositAmount);
#         self.currentAmount=self.currentAmount+depositAmount;
#     def showDetials(self):
#         print("Name: ",self.name);
#         print("Age: ",self.age);
#         print("ID: ",self.id)
# b1=Bank("XYZ",19,2);
# b1.showDetials();
# b1.deposit(200000);
# b1.withdraw(50000);

#inheritance: child class inherit properties from the parent class
#parent cant accessthe properties of child class only child can
#Super keyword= to override the constructor
# class A:  #parent class
#     def showA(self):  
#         print("A");
# class B(A):  #child class
#     def showB(self):
#         print("B")

# obj=B(); # object for child class
# obj.showB();
# obj.showA();  #inheriting the properties from A parent class

# class vehicle:
#     def __init__(self,model, color):#parent class constructor
#         self.model=model;
#         self.color=color;
#     def show(self):
#         print("Car Model: ", self.model);
#         print("Car color: ", self.color);

# class Car(vehicle): #child class
#     def __init__(self,model,color,seat):
#         super().__init__(model,color); #calling the parent constructor
#         self.seat=seat;  #whenever want to call from parent use super keyword
#     def show(self):
#         super().show(); #call the method form parent class , no need to write the implementation part again, call show function for parent class
#         print("Seats are: ", self.seat);

# # v1 = vehicle("Creta", "White")
# # v1.show()
# c1=Car("Creta", "White", 5);
# c1.show();


#inheritance Type:
#--> Single  Level--> One parent one child
# #--> Multilevel-->  A parent of B parent of C --> B is inherited from A, C from B

# class A:
#     def showA(self):
#         print("A");
# class B(A):
#     def showB(self):
#         print("B");
# class C(B):
#     def showC(self):
#         print("C");
# obj=B();
# obj.showA();
# obj.showB();
# obj.showC();

# obj=C();
# obj.showA();
# obj.showB();
# obj.showC();


#--> hierarchy- single parent , multiple child

class A:
    def showA(self):
        print("A");
class B(A):
    def showB(self):
        print("B");
class C(A):
    def showC(self):
        print("C");
# obj=B();
# obj.showA();
# obj.showB();
# obj.showC();

obj=C();
obj.showA();
obj.showB();
obj.showC();




#Method Overriding
# class A:
#     def display(self):
#         print("A Method.....");
# class B(A):
#     def display(self):
#         #how to print a method befor b method
#         super().display(); #super works for parent method or constructor, call the display method which belons to parent(A) class
#         print("B Method.....");
#how to print a method befor b method

# obj = B();
# print(isinstance(obj,A));
# obj.display();


#--> multiple--> a child can have multiple parents
class A:
    # def hello(self):
    #     print("Hello");
    def show(self):
        print("A");

class B(A):
    def show(self):
        super().show();
        print("B");
class C(A):
    def show(self):
        super().show();
        print("C");
class D(B,C):
    def show(self):
        super().show();
        print("D");

obj=D();
obj.show()
# print(D.mro())
# obj.show();
# obj.hello();
#   A
#B      C                       this is known as diamond probelem
#   D

#MRO--> Method resolution order
#used to check the route how D will reach to A
#to check the execution path


#Inheritance--> reusability
#polymorphism-->
#encapsulation--> data security
#Abstraction--> access control, hiding the implementation part, to hide unneccessary info

