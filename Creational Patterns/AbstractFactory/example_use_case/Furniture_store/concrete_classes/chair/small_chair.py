from interface_classes.chair_interface import IChair

# concrete class
class SmallChair(IChair):

    def __init__(self):
        self.height = 20
        self.width = 20
        self.length = 20

    def get_dimensions(self):
        return {
            'height': self.height,
            'width': self.width,
            'length': self.length
        }