a = list(input("Enter words: "))
b = ''
n = 1
for i in a:
    if i == ' ' and b != '':
        print(n, b)
        b = ''
        n += 1
    if len(b) < 10 and i != ' ':
        b += i
print(n, b)

