from abc import ABCMeta, abstractmethod

# Interface class
class IChair(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_dimesions():
        "Interface class dimensions"

