import matplotlib.pyplot as plt 
import numpy as np 

def parabola (a = 1, b = 1, c = 0, tittle = 'parab'):

  x = np.arange(-10, 10, 0.001)
  y = a*x**2 + b*x + c

  plt.plot(x,y)
  plt.show()

#parabola()

def gip (a = 1):

  x = np.arange(-10, 10, 0.001)
  y = a*x**0.5

  plt.plot(x,y)
  plt.show()

gip()