from inteface import IChair

#concrete class subclassing Interface

class SmallChair(IChair):

    def __init__(self):
        self.length = 20
        self.width = 20
        self.height = 20

    def get_dimesions(self):
        return {
            "length": self.length,
            "width": self.width,
            "height": self.height
        }