import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

t = np.arange (-1, 1, 0.1)

def diff_fumc(s, t):
  y, x = s 
  dxdt = 
  dydt = 

  return dxdt, dydt

x0 = 5
y0 = -7

s0 = x0, y0



solve = odeint(diff_fumc, s0, t )
plt.plot(t, solve[:,0],  'b', label = 'sdf')
plt.show()