import math

class Punto():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def setX(self,x):
        self.x=x
    def setY(self,y):
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distanza_origine_punto(self):
        return math.sqrt(self.x**2.0 + self.y**2.0)
