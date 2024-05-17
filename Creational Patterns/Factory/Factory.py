# Factory design pattern
from abc import ABCMeta, abstractmethod

# Class Interface

class Iproduct(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract method"

#A concrete class that implements the interface
class ProductA(Iproduct):

    def __init__(self):
        self.name = "Concrete Product A"

    def create_object(self):
        return self
    
#A concrete class that implements the interface
class ProductB(Iproduct):

    def __init__(self):
        self.name = "Concrete Product B"

    def create_object(self):
        return self
    
#A concrete class that implements the interface
class ProductC(Iproduct):

    def __init__(self):
        self.name = "Concrete Product C"

    def create_object(self):
        return self
    

# Factory Class
class Creator:

    @staticmethod
    def create_object(type):

        if type == 'a':
            return ProductA()
        if type == 'b':
            return ProductB()
        if type == 'c':
            return ProductC()
        
# The Client
Product = Creator().create_object('a')
print(Product.name)

        

