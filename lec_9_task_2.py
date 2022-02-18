import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)
def radiation(m, t):
  dmdt = -k * m * t
  return dmdt


m_0 = 1000
k = 0.08

solve = odeint(radiation, m_0, t)

plt.plot(t, solve[:,0], label = 'raspad')
plt.show()