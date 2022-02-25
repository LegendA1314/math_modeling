import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(1, 25, 0.1)


def razmer(S, t):
  dsdt = 2 * r *(np.pi * S * r * S * np.cos (np.pi - (t - 12) / t))**2
  return dsdt
  
S = 1600
r = 1360

solve= odeint(razmer, S, t)

plt.plot(t, solve[:, 0])
plt.show()