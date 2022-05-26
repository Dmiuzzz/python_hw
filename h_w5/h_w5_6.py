my_f = open("5_6.txt", "r", encoding='utf-8')
new_f = {}
key = ""
word = ""
num = 0
digit = ""
for line in my_f:
    word = ""
    num = 0
    for i in line:
        if i != ":":
            word += i
        if i == ":":
            key = word
            word = ""
        if i.isdigit():
            digit += i
        elif digit == "":
            continue
        else:
            num += int(digit)
            digit = ""
        new_f[key] = num
my_f.close()
print(new_f)




# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}