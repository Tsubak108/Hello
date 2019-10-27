ravenue = int(input("Введите прибыль: "))
costs = int(input("Введите издержки: "))
if ravenue > costs:
    profit = ravenue-costs
    rent = profit/ravenue
    print(f"Отлично.  {profit}  выручка")
    people = int(input("Сколько у вас работников: "))
    print(f"{profit/people} на одного работника")
elif ravenue == costs:
    print("Не плохо")
else:
    print(" Пора закрывать фирму))")