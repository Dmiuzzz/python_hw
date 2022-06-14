my_list = (el for el in range(20, 240) if el % 21 == 0 or el % 22 == 0)
for i in my_list:
    print(i)