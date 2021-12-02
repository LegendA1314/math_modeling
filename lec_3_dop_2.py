import numpy as np

a = np.ones((5, 5))

for i in range(5):
 for j in range(5):
  print("Элемент i, j:",i,j)
  a[i,j] = input()

a[5, 5] = 0

k = input("что вставить?")
l = input("куда вставить?(j)")
v = input("куда()i")


