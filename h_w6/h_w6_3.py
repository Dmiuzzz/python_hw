class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])

p = Position("Bob", "Slim", "водитель", 10000, 5000)
p.get_full_name()
p.get_total_income()
print(p.position)

