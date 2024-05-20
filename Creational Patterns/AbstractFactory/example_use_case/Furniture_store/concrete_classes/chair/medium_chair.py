from interface_classes.chair_interface import IChair

# concrete class
class MediumChair(IChair):

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