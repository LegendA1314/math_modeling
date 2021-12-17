print('Введите число, которому соответствует фигура 1 - круг, 2 - треугольник, 3  - прямоугольник ')
p = int(input())

if p == 1:
  a = int(input())
  def krug (a):
    v = a**2 *3.14
    return a
  print(krug(a))
elif p == 2:
  a = int(input())
  b = int(input())
  def trey (a, b):
    m = a * b * 0.5
    return m
  print(trey(a, b))
elif p == 3:
  a = int(input())
  b = int(input())
  def pryam (a, b):
    l = a * b
    return l
  print(pryam(a,b))
else:
  a = int(input())
  def af (a):
    a = "НЕТ "
    return a
  print (af(a))