from functools import reduce
my_list =(el for el in range(100, 1001) if el % 2 == 0)
def sumoist(x, y):
    return x + y
print(reduce(sumoist, my_list))