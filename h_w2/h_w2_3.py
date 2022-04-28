n = int(input("Enter the month number "))
if n == 12:
    key = 0
else:
    key = n // 3
my_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}
print(my_dict.get(key))
