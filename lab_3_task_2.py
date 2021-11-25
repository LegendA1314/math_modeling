import numpy as np
import math
from lab_3_task_1 import earth as g
from lab_3_task_1 import bol as k
from lab_3_task_1 import eiler as i 
from lab_3_task_1 import plan as p 

h = 100 
a = math.pi / 3
b = 30
t = 200 
e = 300 


v = ((g*h*(math.tan(b))**2)/(2*(math.cos(a))**2*(1-math.tan(b)*math.tan(b))))**2

print(v)

n = ((2/(math.pi)**0.5) * (p/(k*t)**(3/2)) * (i**(-e/(p*t)) * (e**(t/2)))

print(n)