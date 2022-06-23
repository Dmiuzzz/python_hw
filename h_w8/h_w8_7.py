class Complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __mul__(self, other):
        return self.a * other.a, self.b * other.b

obj1 = Complex_number(1, 2)
obj2 = Complex_number(-1, -2)
print(obj1 + obj2)
print(obj1 * obj2)