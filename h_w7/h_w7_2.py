class Clothes:
    pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v
    @property
    def s_mat(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, h):
        self.h = h
    @property
    def s_mat(self):
        return 2 * self.h + 0.3

co = Coat(52)
print(co.s_mat)
su = Suit(180)
print(su.s_mat)
print(co.s_mat+su.s_mat)