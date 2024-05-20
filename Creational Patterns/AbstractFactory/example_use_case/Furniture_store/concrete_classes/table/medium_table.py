from interface_classes.table_interface import ITable

# concrete class
class MediumTable(ITable):

    def __init__(self):
        self.height = 40
        self.width = 40
        self.length = 40

    def get_dimensions(self):
        return {
            'height': self.height,
            'width': self.width,
            'length': self.length
        }