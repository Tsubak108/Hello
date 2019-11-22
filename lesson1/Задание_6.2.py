class Cars:
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        if direction == 'left':
            print(f'Машина {self.name} повернула налево')
        if direction == 'right':
            print(f'Машина {self.name} повернула направо')


class TownCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self.is_police = False


class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self.is_police = False

class WorkCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self.is_police = False

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self.is_police = True

one_town_car = TownCar('town car', 100, 'red')
one_sport_car = SportCar('sport car', 200, 'green')
one_work_car = WorkCar('work car', 50, 'blue')
one_police_car = PoliceCar('police car', 100, 'dark')

print(one_police_car.is_police)
print(one_sport_car.is_police)
one_town_car.go()
one_sport_car.stop()
one_work_car.turn('left')
one_police_car.turn('right')