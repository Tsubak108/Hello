ravenue = int(input("Введите прибыль: "))
costs = int(input("Введите издержки: "))
if ravenue > costs:
    profit = ravenue - costs
    rent = profit / ravenue
    print(f"Отлично.  {profit}  выручка и {rent} рентабельность")
    people = int(input("Сколько у вас работников: "))
    print(f"{profit / people:.2f} на одного работника")
elif ravenue == costs:
    print("Не плохо")
else:
    print(" Пора закрывать фирму))")
