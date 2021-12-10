import numpy as np
l = int(input())
k = int(input())

a = np.zeros((l,k))

for i in range (l):
  for j in range (k):
    a[i, j] = float(input())

for i in range (l):
  for j in range (k):
    