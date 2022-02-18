import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)
def radiation(m, t):
  dmdt = k * m
  return dmdt


m_0 = 2
k = 5

solve_bi = odeint(radiation, m_0, t)

plt.plot(t, solve_bi[:,0], label = 'raspad')
plt.show()