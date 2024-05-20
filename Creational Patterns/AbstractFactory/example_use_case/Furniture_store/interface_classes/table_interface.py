from abc import ABCMeta, abstractmethod

# Interface class for chair
class ITable(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "Interface method "
        