n = 5

def fuct(n):
    fuct = 1
    for i in range(1, n+1):
        fuct *= i
        yield fuct

for el in fuct(n):
    print(el)