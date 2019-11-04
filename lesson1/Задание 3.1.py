def my_del():
    val_1 = int(input('Введие значение первого аргумента: '))
    val_2 = int(input('Введите значение второго аргумента: '))
    if val_2 != 0:
        return val_1 / val_2
    else:
        print("Неверное значение! На 0 делить нельзя")

print(f'Результат {my_del()}')