class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight(self):
        return f'{self._length} m * {self._width} m *25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т'


a = Road(10000, 15)
print(a.get_weight())
