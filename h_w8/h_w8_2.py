class StupidError(Exception):
  pass

try:
  inp_num1 = int(input('Введите делимое число: '))
  inp_num2 = int(input('Введите делитель: '))
  if inp_num2 == 0:
    raise StupidError("ZeroDivisionError")
except StupidError as e:
  print(e)
else:
  print(f"Result = {inp_num1/inp_num2}")
