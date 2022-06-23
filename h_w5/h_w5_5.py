my_f = open("5_5.txt", "w")
sumoist = 0
my_f.write("1 3 5 7")
my_f.close()
my_f = open("5_5.txt", "r")
content = my_f.read().split()
for i in content:
    sumoist += int(i)
print(sumoist)
my_f.close()
