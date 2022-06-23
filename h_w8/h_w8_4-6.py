class Warehouse:
    def __init__(self):
        self._dict = {}
    def warehousing(self, appliances):
        try:
            quantity = int(input(f"Введите количество {appliances.name} {appliances.model} "))
        except ValueError:
            print('Введите число!')
        self._dict.setdefault(appliances.group_name(), []).append(appliances)
        self._dict.setdefault(appliances.group_name(), []).append(quantity)
    def transfer(self, name, model):
        for key in self._dict:
            count = 0
            for nm in self._dict[key]:
                if not nm.find(f'{name} {model}'):
                    self._dict[key].pop(count)
                count += 1

class Of_app:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.group = self.__class__.__name__
    def group_name(self):
        return f'{self.group}'

class Printer(Of_app):
    def __init__(self, name, model, type):
        Of_app.__init__(self, name, model)
        self.type = type
    def __repr__(self):
        return f"'{self.name} {self.model} {self.type}'"

class Scanner(Of_app):
    def __init__(self, name, model, speed):
        Of_app.__init__(self, name, model)
        self.speed = speed
    def __repr__(self):
        return f"'{self.name} {self.model} {self.speed}'"

class Copier(Of_app):
    def __init__(self, name, model, paper_size):
        Of_app.__init__(self, name, model)
        self.paper_size = paper_size
    def __repr__(self):
        return f"'{self.name} {self.model} {self.paper_size}'"

wh = Warehouse()
printer1 = Printer('HP', 'CY23-7', 'color')
wh.warehousing(printer1)
scaner1 = Scanner('apple', 'NF23-7', 2000)
wh.warehousing(scaner1)
copier1 = Copier('Canon', 'REM3-7', 'A4')
wh.warehousing(copier1)
copier1 = Copier('Canon', 'FUR3-7', 'A1')
wh.warehousing(copier1)
print(wh._dict)
#wh.transfer('Canon', 'REM3-7')
#print(wh._dict)
