my_list = [7, 5, 3, 3, 2]
print(my_list)
digit = int(input("Введите число (111 - выход"))
for el in range(len(my_list)):
    if my_list[el] == digit:
        my_list.insert(el + 1, digit)
        break
    elif my_list[0] < digit:
        my_list.insert(0, digit)
        break
    elif my_list[-1] > digit:
        my_list.append(digit)
        break
    elif my_list[el] > digit and my_list[el + 1] < digit:
        my_list.insert(el + 1, digit)
        break

print(my_list)
