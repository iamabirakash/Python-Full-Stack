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
