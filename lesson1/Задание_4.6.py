from itertools import count

for el in count(int(input('Введите стартовое число: '))):
    print(el) # Бесконечный цикл

from itertools import cycle

list = [False, 'ABC', 145, None]
for el in cycle(list):
    print(el) # Бесконечный цикл