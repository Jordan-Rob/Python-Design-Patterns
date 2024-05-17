from factory import ChairFactory

Chair = ChairFactory().get_chair('s')
print(Chair.get_dimesions())