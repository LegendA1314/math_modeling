a = input(('Введите первую сторону '))
b = input(('Введите вторую сторону '))
c = input(('Введите третью сторону '))

if a <= b + c or b <= a + c or c <= a + b:
  print ('Треугольник существует')

  if a == c or a == b or b == c:
    print("Треугольник равнобедренный")
  elif a == b == c:
    print("Треугольник равносторонний ")
  else:
    print("Треугольник разносторонний")

else:
  print("Треугольник не существует")

