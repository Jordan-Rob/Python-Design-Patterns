from interface_classes.chair_interface import IChair

# concrete class
class LargeChair(IChair):

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