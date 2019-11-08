a = [1, 3, 5, 7, 2, 10, 22, 55, 4]
b = [el for num, el in enumerate(a) if a[num - 1] < a[num]]

print(f'Исходный список {a}')
print(f'Новый список {b}')