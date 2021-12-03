import numpy as np

a = np.ones((5, 1))

for i in range(5):
 for j in range(1):
  print("Элемент i, j:",i,j)
  a[i,j] = input()

a[5, 1] = 0

k = input("что вставить?")
v = input("куда(i)")



