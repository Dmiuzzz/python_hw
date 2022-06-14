my_t = open("5_2.txt", "r")
n = 1
w = 0

for line in my_t:
    w = len(line.split())
    print(f"В {n} cторке - {w} слов(а)")
    n += 1
my_t.close()