class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
    def asphalt_mass(self, mass_1m, thick):
        return self._length * self._width * mass_1m * thick

r = Road(20, 40)
print(r.asphalt_mass(30, 0.2))
