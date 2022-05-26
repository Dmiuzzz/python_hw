import json

data = open("5_7.txt", "r")
data_dic = {}
res_dic = {}
report = []
n = 0
total_profit = 0

for line in data:
    firm_d = line.split()
    if int(firm_d[2]) - int(firm_d[3]) > 0:
        profit = int(firm_d[2]) - int(firm_d[3])
        data_dic[firm_d[0]] = profit
        total_profit += profit
        n += 1
    elif int(firm_d[2]) - int(firm_d[3]) == 0:
        continue
    elif int(firm_d[2]) - int(firm_d[3]) < 0:
        data_dic[firm_d[0]] = "loss"

data.close()
res_dic["average_profit"] = round(total_profit/n, 2)
report.append(data_dic)
report.append(res_dic)

with open("my_file.json", "w") as write_f:
  json.dump(report, write_f)
