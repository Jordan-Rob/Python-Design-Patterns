from concrete_classes.chair.small_chair import SmallChair
from concrete_classes.chair.medium_chair import MediumChair
from concrete_classes.chair.large_chair import LargeChair

# Factory class
class ChairFactory:

    @staticmethod
    def get_chair(size):
        try: 
            if "small" in size:
                return SmallChair()
            if 'medium' in size:
                return MediumChair()
            if 'large' in size:
                return LargeChair()
        except Exception as _e:
            print(_e)
        return None