from abstract_factory import AbstractFactory

product = AbstractFactory().create_object('ab')
print(f"{product.__class__}")

product = AbstractFactory().create_object('bc')
print(f"{product.__class__}")