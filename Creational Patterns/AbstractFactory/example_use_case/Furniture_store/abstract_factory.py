from abc import ABCMeta, abstractmethod
from factory_classes.chair_factory import ChairFactory
from factory_classes.table_factory import TableFactory

# Factory interface
class IFactory(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_object(factory):
        "interface factory class"


class FurnitureFactory(IFactory):

    @staticmethod
    def create_object(factory):

        try:
            if "Chair" in factory:
                return ChairFactory.get_chair(factory)
            if "Table" in factory:
                return TableFactory.get_table(factory)
        except Exception as _e:
            print(_e)
        return None