def func5(*args):
    a = 0
    b = 0
    x = []
    y = ''

    while a == 0:
        x = (input("Введите цифры через пробел: "
                   "Enter - что бы узнать сумму, Введите Q + Enter для выхода"))
        for i in x:
            if i == 'Q':
                a = 1
                break
            y += i

        b += sum(list(map(int, y.split())))
        y = ''
        if a == 0:
            print(b)
    return(b)

print(func5())