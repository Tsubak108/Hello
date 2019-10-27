a = float(input("Старт: "))
b = float(input("Финиш: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)