from small_chair import SmallChair
from medium_chair import MediumChair
from large_chair import LargeChair

# Factory class 

class ChairFactory:

    @staticmethod
    def get_chair(chair_size):

        if chair_size == 's':
            return SmallChair()
        if chair_size == 'm':
            return MediumChair()
        if chair_size == 'l':
            return LargeChair()
        
        return None
    
