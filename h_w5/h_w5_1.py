text_inp = open("text_inp.txt", "w")
c = 0
while True:
    t = text_inp.write(input("Введите текст. 2 раза Enter для выхода" ))
    if t == 0:
        break
    text_inp.write("\n")

text_inp.close()