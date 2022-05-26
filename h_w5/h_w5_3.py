import codecs

my_t = codecs.open("5_3.txt", "r", "utf-8")
# без codecs была ошибка UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 1: character maps to <undefined>

sum = 0
list_l = []
n = 0

for line in my_t:
   list_l = line.split()
   if float(list_l[1]) < 20000:
      print(list_l[0])
   sum += float(list_l[1])
   n += 1

my_t.close()

print(f"Средняя величина дохода сотрудников {round(sum/n,2)}")