revenue = int(input('Введите значение выручки : '))
costs = int(input('Введите значение издержки: '))
if revenue > costs:
    profit = revenue - costs
    rent = profit/revenue
    print(f"Отлично, {profit} прибыль")
    people = int(input("Введите количество работников: "))
    print (f" {profit/people} на одного работника")
elif revenue == costs:
    print("Не плохо")
else:
    print ("Пора закрывать фирму -) ")