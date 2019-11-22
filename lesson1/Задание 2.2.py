count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
l = 0
while i < count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list) / 2)):
    my_list[l], my_list[l + 1] = my_list[l + 1], my_list[l]
    l += 2
print(my_list)
