class Vehicle:

    def __init__(self):
        self.wheels = int()

    def getSpeed(self):
        pass


class Car(Vehicle):

    def __init__(self):
        self.speed = float()

    def accelerate(self, rate):
        pass

    def decelerate(self):
        pass


class Truck(Vehicle):

    def __init__(self):
        self.mpg = float()

    def tryHard(self, rate, speed, look):
        pass


class Ford150(Truck):

    def __init__(self):
        pass
