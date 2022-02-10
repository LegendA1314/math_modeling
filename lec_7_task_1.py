import matplotlib.pyplot as plt
import numpy as np
a = float(input())

if a == 1:
  def a():
    a = np.arange(-2*np.pi, 2*np.pi, 0.1)
    R = 3

    
    x = R * (a - np.sin(a)**3)

    y = R * (1 - np.cos(a)**3)

    plt.plot(x, y, ls='--', lw=3)
    plt.axis('equal')
    plt.show()

  a()
  
else:
  def b():
    a = np.arange(-2*np.pi, 2*np.pi, 0.1)
    R = 3

      
    x = R * np.cos(a)**3

    y = R * np.sin(a)**3

    plt.plot(x, y, ls='--', lw=3)
    plt.axis('equal')
    plt.show()

  b()