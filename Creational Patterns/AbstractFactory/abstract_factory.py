from abc import ABCMeta, abstractmethod
from factory_a import FactoryA
from factory_b import FactoryB

# Interface of abstract factory
class IAbstractFactory(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_object(factory):
        "interface of abstract factory class"

# Abstract Factory class implementing above interface
class AbstractFactory(IAbstractFactory):

    @staticmethod
    def create_object(factory):
        # get_factory static method 

        try:
            if factory in ['aa', 'ab', 'ac']:
                return FactoryA().get_product(factory[1])
            if factory in ['ba', 'bb', 'bc']:
                return FactoryB().get_product(factory[1])
            raise Exception('No factory found')
        except Exception as _e:
            print(_e)
        return None
    
