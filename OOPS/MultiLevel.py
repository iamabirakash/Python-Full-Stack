class Vehicle:
    def show(self):
        print("This is Vehicle")
class Car(Vehicle):
    def info(self):
        print("This is Car")
class EV(Car):
    def display(self):
        print("This is an EV Car")

ev = EV()
ev.show()
ev.info()
ev.display()