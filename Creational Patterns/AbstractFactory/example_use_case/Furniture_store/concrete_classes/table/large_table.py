from interface_classes.table_interface import ITable

# concrete class
class LargeTable(ITable):

    def __init__(self):
        self.height = 60
        self.width = 60
        self.length = 60

    def get_dimensions(self):
        return {
            'height': self.height,
            'width': self.width,
            'length': self.length
        }