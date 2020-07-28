# ******************Abstract Base Class*****************
# Abstract class force the other classes who is inherit from it to
# define functions which are in abstract base classfrom abc import ABC, abstractmethod
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type ="Rectangle"
    sides = 4
    def __init__(self):
        self.length=6
        self.breadth=8

    def printarea(self):
        return self.length*self.breadth
rect= Rectangle()
print(rect.printarea())