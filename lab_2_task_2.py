a = int(input('Введите первый член прогресии '))
b  = int(input("Введите знаменатель прогресии "))
c = int(input("Введите колво членов прогресии "))
i = 1
n = 1

while i < c:

  d = a * b**(n-1)
  n += 1
  i += 1
  print(n,  d)
  