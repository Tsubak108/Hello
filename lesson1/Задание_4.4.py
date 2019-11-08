list = [4, 5, 22, 12, 40, 32, 30, 78, 100, 5, 22, 4]
new_list = [el for el in list if list.count(el) < 2]
print(new_list)