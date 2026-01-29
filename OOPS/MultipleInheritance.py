class Camera:
    def __init__(self,pixel):
        self.pixel = pixel
    def show(self):
        print("MegaPixels :-",self.pixel)

class Phone:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Phone :-",self.name)

class smartphone(Camera,Phone):
    def __init__(self, pixel, name, model):
        Camera.__init__(self,pixel)
        Phone.__init__(self,name)
        self.model = model
    def info(self):
        self.show()
        self.display()
        print("Model :-",self.model)
    
s = smartphone(10,"Apple",17)
s.info()