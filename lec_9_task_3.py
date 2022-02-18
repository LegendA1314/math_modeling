import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 60, 0.1)
def radiation(v, t):
  dvdt = F/m -  gamma * v**2 / m
  return dvdt


F = 1
m = 5
gamma = 0.3
v0 =10

solve = odeint(radiation, v0, t)

plt.plot(t, solve[:,0], label = 'raspad')
plt.show()