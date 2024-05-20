from abstract_factory import FurnitureFactory

product = FurnitureFactory().create_object('smallChair')
print(f"{product.__class__} : {product.get_dimensions()}")

product = FurnitureFactory().create_object('largeTable')
print(f"{product.__class__} : {product.get_dimensions()}")
