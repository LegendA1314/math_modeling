a = float(input('Введите первый коофицент '))
b = float(input('Введите второй коофицент '))
c = float(input('Введите третий коофицент '))

d = b**2 - 4 * a * c

if d > 0:
  x1 = ((-b + d**0.5) / (2 * a))
  x2 = ((-b + d**0.5) / (2 * a))
  print (f'Первый корень = {x1} , Второй = {x2} ')
elif d == 0:
  x= ((-b) / (2 * a))
  print (f'Корень равен {x}')
else:
  print ("Нет корней")
