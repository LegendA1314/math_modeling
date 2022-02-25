import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 24, 0.1)


def razmer(s, t):
  dsdt = k * np.sqrt(s/np.pi) * e *s * np.cos((np.pi/12)*(t-12))
  return dsdt
  
S = 16
e = 1360
k = 2

solve= odeint(razmer, S, t)

plt.plot(t, solve[:, 0])
plt.show()