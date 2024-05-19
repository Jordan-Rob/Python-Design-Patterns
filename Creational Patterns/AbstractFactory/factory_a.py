from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"

# concrete classes implementin above Interface class

class ProductA(IProduct):

    def __init__(self):
        self.name = "Product A"

    def create_object(self):
        return self
    
class ProductB(IProduct):

    def __init__(self):
        self.name = "Product B"

    def create_object(self):
        return self
    
class ProductC(IProduct):

    def __init__(self):
        self.name = "Product C"

    def create_object(self):
        return self
    
# Factory class interacting with concrete classes
    
class FactoryA:

    @staticmethod
    def get_product(some_property):
        try:
            if some_property == 'a':
                return ProductA()
            elif some_property == 'b':
                return ProductB()
            elif some_property == 'c':
                return ProductC()
            raise Exception('Class not found')
        except Exception as _e:
            print(_e)
        return None
    
    