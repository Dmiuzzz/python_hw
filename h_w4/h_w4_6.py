from itertools import count, cycle

count_list = []
cycle_list = []
c = 0
for el in count(3):
    if el > 10:
        break
    count_list.append(el)

print(count_list)

for el in cycle('123'):
    if c > 10:
        break
    cycle_list.append(el)
    c += 1

print(cycle_list)