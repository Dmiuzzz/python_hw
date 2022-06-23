my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_my_list = (my_list[i+1] for i in range(len(my_list)-1) if my_list[i+1] > my_list[i])

a = []
for i in new_my_list:
    a.append(i)
print(a)

