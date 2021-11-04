a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c

if d > 0:
  x1 = ((-b + d) / (2 * a))
  x2 = ((-b + d) / (2 * a))
  print (f'Первый корень = {x1} , Второй = {x2} ')
elif d == 0:
  x= ((-b) / (2 * a))
  print (f'Корень равен {x}')
else:
  print ("Нет корней")
