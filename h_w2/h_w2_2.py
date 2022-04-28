a = []
n = int(input("Enter number of elements: "))
for i in range(0, n):
    el = int(input("Enter element"))
    a.append(el)
b = []
for i in range(0, len(a), 2):
    if a[i] != a[-1]:
        b.append(a[i+1])
    b.append(a[i])
print(a)
print(b)