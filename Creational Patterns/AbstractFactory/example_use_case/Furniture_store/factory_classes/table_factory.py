from concrete_classes.table.small_table import SmallTable
from concrete_classes.table.medium_table import MediumTable
from concrete_classes.table.large_table import LargeTable

# Factory class
class TableFactory:

    @staticmethod
    def get_table(size):
        try: 
            if "small" in size:
                return SmallTable()
            if 'medium' in size:
                return MediumTable()
            if 'large' in size:
                return LargeTable()
        except Exception as _e:
            print(_e)
        return None