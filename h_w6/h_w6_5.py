class Stationery:
    title = ""
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    def draw(self):
        print("Синяя линия")

class Pencil(Stationery):
    def draw(self):
        print("Черная линия")

class Handle(Stationery):
    def draw(self):
        print("Жирная линия")

s = Stationery()
s.draw()

p = Pen()
p.draw()

pe = Pencil()
pe.draw()

h = Handle()
h.draw()