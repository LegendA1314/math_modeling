from lab_3_task_4 import A as A
from lab_3_task_4 import M as M
from lab_3_task_4 import N as N
import numpy

for i in range (N):
  for j in range (M):
    A[i, j], A[i, j]= A[i, j], A[i, j]

print (A)