import numpy as np 
import math

N = 3
M = 6
st = 1
A = np.ones((N, M))

if st == 0:
  for i in range(N-1):
   for j in range(M-1):
    A[i,j]=math.sin(N * (i+1) + M * (j + 1))
else:
  for i in range(1,N-1):
   for j in range(1,M-1):
    A[i,j]=math.sin(N * i + M * j)
 
print(A)


