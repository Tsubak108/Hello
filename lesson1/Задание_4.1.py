def my_money():
    try:
        time = float(input('Введите выработку в часах: '))
        sal = int(input('Введите ставку в у.e: '))
        bonus = int(input('Введите премию в у.е: '))
        zarpl = time * sal + bonus
        print(f'Заработная плата: {zarpl}')
    except ValueError:
        return print('Не номер')

my_money()



