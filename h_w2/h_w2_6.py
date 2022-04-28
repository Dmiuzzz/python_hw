d_list = []
d_tuple = ()
for i in range(3):
    d_tuple =(i + 1, {"название": input("название "), "цена": int(input("цена ")), "количество":
        int(input("количество ")), "ед": input("ед ")})
    d_list.append(d_tuple)
print(d_list)
list_name = []
list_price = []
list_num = []
list_p = []
for i in d_list:
    list_name.append(i[1]["название"])
    list_price.append(i[1]["цена"])
    list_num.append(i[1]["количество"])
    list_p.append(i[1]["ед"])
a_dict = {}
list_name = list(set(list_name)) # проверка на уникальность
list_price = list(set(list_price))
list_num = list(set(list_num))
list_p = list(set(list_p))
a_dict = {"название": list_name, "цена": list_price, "количество": list_num, "ед": list_p}

print(a_dict)