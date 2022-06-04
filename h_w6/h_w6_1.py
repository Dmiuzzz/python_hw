import time

class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]
    def running(self):
        for i in TrafficLight.__color:
            print(i)
            if i == TrafficLight.__color[0]:
                time.sleep(7)
            elif i == TrafficLight.__color[1]:
                time.sleep(2)
            elif i == TrafficLight.__color[2]:
                time.sleep(7)

t = TrafficLight()
t.running()
