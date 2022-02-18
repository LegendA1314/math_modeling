import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10**6,100)
def radiation(m, t):
  dmdt = -k * m
  return dmdt


m_0 = 10
k = 1.61*10**(-6)

solve_bi = odeint(radiation, m_0, t)

plt.plot(t, solve_bi[:,0], label = 'raspad')
plt.show()