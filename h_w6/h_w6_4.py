class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print("Автомобиль едет")
    def stop(self):
        print("Автомобиль остановился")
    def turn(self, turn):
        if turn == "влево":
            print("Автомобиль повернул налево")
        if turn == "вправо":
            print("Автомобиль повернул направо")
    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена")
        else:
            print(self.speed)

class SportCar(Car):
    def show_speed(self):
        if self.speed < 250:
            print("Это не Sportcar")
        else:
            print(self.speed)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Скорость превышена")
        else:
            print(self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.is_police == False:
            print("Это не PoliceCar")

t = TownCar(65, "Red", "Lamba", False)
t.show_speed()
t.turn("вправо")

s = SportCar(160, "black", "Fera", False)
s.show_speed()
s.turn("вправо")

p = PoliceCar(160, "black", "Fera", False)
p.turn("влево")
