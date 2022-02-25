import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(1, 25, 0.1)


def razmer(S, t):
  o = k * (s/np.pi)**0.5 * r *s * np.cos((np.pi/12)*(t-12))
  return o
  
S = 1600
r = 1360
k = 2

solve= odeint(razmer, S, t)

plt.plot(t, solve[:, 0])
plt.show()