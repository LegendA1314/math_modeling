import matplotlib.pyplot as plt
import numpy as np

if 
def krug (r=5):

  x = np.arange (-2*r, 2*r, 0.1)
  y = np.arange (-2*r, 2*r, 0.1)

  X, Y = np.meshgrid(x, y)

  xy = X**2 + Y**2

  plt.contour(X, Y, xy, levels=[r**2])
  plt.axis('equal')
  plt.show()

#krug()

def elip (r=5):
  x = np.arange (-2*r, 2*r, 0.1)
  y = np.arange (-2*r, 2*r, 0.1)

  X, Y = np.meshgrid(x, y)

  xy = X**2/2.5 + Y**2/5  

  plt.contour(X, Y, xy, levels=[r**2])
  plt.axis('equal')
  plt.show()

elip()