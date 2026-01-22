# Step 1: Define a CLass named 'Car' with attributes for Company, Model, Year, Speed.
# class Car:
#     company = "None"
#     model = "None"
#     year = 0
#     speed = 0

# my_car =  Car()
# print(my_car)
# print(my_car.company)
# print(my_car.year)

# Step 2: No Linkage
# class Car:
#     def __init__(make,model,year):
#         make = make
#         model = model
#         year = year

# my_car = Car("Thar")
# print(my_car)

# Step 3: Link the attribute to the self, Linkage
# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year

# my_car = Car("Mahindra","Thar",2022)
# print(my_car)
# print("Make :-",my_car.make)
# print("Model :-",my_car.model)
# print("Year :-",my_car.year)

# Step 4: Additional
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print("Acceleration Speed :-",self.speed)

    def manual_accelerate(self,speed):
        self.speed += speed
        print("Manual Acceleration Speed :-",self.speed)

    def brake(self):
        self.speed -= 5
        print("Brake Speed :-",self.speed)

    def manual_brake(self,speed):
        self.speed -= speed
        print("Manual Brake Speed :-",self.speed)

my_car = Car("Mahindra","Thar",2022)
print(my_car)
print("Make :-",my_car.make)
print("Model :-",my_car.model)
print("Year :-",my_car.year)
my_car.accelerate()
my_car.manual_accelerate(20)
my_car.brake()
my_car.manual_brake(2)