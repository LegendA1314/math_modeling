import numpy as np

a = np.zeros((2, 2))
b = np.zeros((2, 2))
c = np.zeros((2, 2))

print ("введите элементы массива 1")

for i in range(2):
 for j in range(2):
  print("Элемент i, j:",i,j)
  a[i,j] = input()

print ("введите элементы массива 2")

for i in range(2):
 for j in range(2):
  print("Элемент i, j:",i,j)
  b[i,j] = input()

print (f"Массив 1: {a}")
print (f"Массив 2: {b}")

for i in range(2):
 for j in range(2):
  if a[i,j] > b[i, j]:
    c[i, j] = a[i, j]
  else :
    c[i, j] = b[i, j]

print ("Результат")

print(c)