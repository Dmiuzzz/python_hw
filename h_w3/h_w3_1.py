def func1(a, b):
    c = 0
    if b == 0:
        print('ZeroDivisionError')
    else:
        c = a / b
    return(c)

print(func1(int(input('Enter a number ')), int(input('Enter a number '))))
