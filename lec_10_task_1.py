import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

x = np.arange (-5, 5, 0.1)

def diff_fumc(s, x):
  y, z = s 
  dydx = y**2 * z
  dzdx = z/x - y * z**2

  return dydx, dzdx

y0 = 1
z0 = -3

s0 = y0, z0



solve = odeint(diff_fumc, s0, x )
plt.plot( solve[:,1],  'b', label = 'sdf')
plt.show()