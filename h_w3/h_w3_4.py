def my_func1(x, y): return x**y

print(my_func1(3,-7))

def my_func2(x, y):
    p = 1
    for i in range(y, 0):
        p *= 1/x
    return p

print(my_func2(3, -7))