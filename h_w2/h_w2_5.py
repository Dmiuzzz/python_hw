my_list = [7, 5, 3, 3, 2]
n = int(input('Enter number: '))
for i in range(5):
    if my_list[i] < n:
        my_list.insert(i, n)
        break
if my_list[-1] > n:
    my_list.append(n)
print(my_list)