import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

t = np.arange (-5, 5, 0.1)

def diff_fumc(o, y):
  y, x = s 
  dxdt = o
  dydt = -4*o - 5 * y

  return dxdt, dydt

dy0dt = -1
y0 = 4

s0 = dy0dt, y0



solve = odeint(diff_fumc, dy0dt, y0 )
plt.plot(t, solve[:,0],  'b', label = 'sdf')
plt.show()