class Cell:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return self.num + other.num
    def __sub__(self, other):
        if self.num - other.num > 0:
            return self.num - other.num
        else:
            return f"Разность <= 0"
    def __mul__(self, other):
        return self.num * other.num
    def __truediv__(self, other):
        return self.num // other.num
    def make_order(self, n):
        string = ''
        for i in range(1, self.num+1):
            string += '*'
            if i % n == 0 and i != self.num:
                string += '\\n'
        return string

c = Cell(15)
c1 = Cell(5)
print(c + c1)
print(c - c1)
print(c * c1)
print(c / c1)
print(c.make_order(5))
