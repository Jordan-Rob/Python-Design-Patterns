from inteface import IChair

#concrete class subclassing Interface

class MediumChair(IChair):

    def __init__(self):
        self.length = 40
        self.width = 40
        self.height = 40

    def get_dimesions(self):
        return {
            "length": self.length,
            "width": self.width,
            "height": self.height
        }