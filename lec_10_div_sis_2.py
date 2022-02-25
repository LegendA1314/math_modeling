import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

t = np.arange (0, 10, 0.1)

def diff_fumc(z, t):
  theta, omega = z 
  dtheta_dt = omega 
  domega_dt = 

  return dtheta_dt, domega_dt

theta0 = np.pi - 0.1 
omega0 = 0

z0 = theta0, omega0

b = 0.25
c = 5.0

solve = odeint(diff_fumc, z0, t)
plt.plot( solve[:,0], solve[:,1],  'g', label = 'sdf')
plt.show()