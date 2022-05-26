en_ru_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

my_f = open("5_4.txt", "r")
out_f = open("new_5_4.txt", "w", encoding='utf-8')

for line in my_f:
    l = line.split()
    l[0] = en_ru_dict[l[0]]
    line = " ".join(l)
    print(line)
    out_f.write(line + '\n')

my_f.close()
out_f.close()