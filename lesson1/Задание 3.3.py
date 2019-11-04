def my_func(val_1, val_2, val_3):
    if val_1 >= val_3 and val_2 >= val_3:
        return val_1 + val_2
    elif val_1 > val_2 and val_1 < val_3:
        return val_1 + val_3
    else:
        return val_2 + val_3

print(f'Результат - {my_func(int(input("Введите 1 элемент ")), int(input("Введите 2 элемент ")), int(input("Введите 3 элемент ")))}')
