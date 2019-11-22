class TownCar:
    speed = 100
    color = "red"
    name = "Renault"
    is_police = False

class SportCar:
    speed = 300
    color = "black"
    name = "Lamborgini"
    is_police = False

class WorkCar:
    speed = 30
    color = "yellow"
    name = "tractor"
    is_police = False

class PoliceCar:
    speed = 250
    color = "white"
    name = "Ford"
    is_police = True

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        if direction == 'left':
            print(f'Машина {self.name} повернула налево')
        if direction == 'right':
            print(f'Машина {self.name} повернула направо')
