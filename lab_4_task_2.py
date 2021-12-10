import numpy as np

a = np.zeros((5, 1))

for i in range(5):
  a[i] = int(input())


def hehe(a):
  n = 1 
  for i in range (5):
    n = n * a[i]
  print (n)
    
hehe(a)