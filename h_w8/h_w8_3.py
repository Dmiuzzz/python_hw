class StupidError(Exception):
  pass

arr = []
while True:
    try:
        inp_num = input('Введите число: или "stop" для выхода ')
        if inp_num == 'stop':
            break
        elif inp_num.isdigit() != True:
            raise StupidError("You input text. Please input number")
    except StupidError as e:
        print(e)
    else:
        arr.append(inp_num)

print(arr)
