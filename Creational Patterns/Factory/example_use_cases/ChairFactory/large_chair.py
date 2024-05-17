from inteface import IChair

#concrete class subclassing Interface

class LargeChair(IChair):

    def __init__(self):
        self.length = 60
        self.width = 60
        self.height = 60

    def get_dimesions(self):
        return {
            "length": self.length,
            "width": self.width,
            "height": self.height
        }