import numpy as np


e = []

for i in range(5):
  e.append(int(input()))

def hehe (a ):
  N = 0
  for i in range (len(a)):
    N = N + a[i] 
  print(N/len(a))
  
hehe(e)