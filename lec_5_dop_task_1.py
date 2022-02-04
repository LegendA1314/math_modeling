import matplotlib.pyplot as plt 
import numpy as np 

def m (a=1,a1=1,b=3,b1=0.5):
 t = np.arange(1, 5, 0.1)

 x = a1 * np.sin(a*t+(np.pi/2))
 y = b1 * np.sin(b*t)

 plt.plot(x,y)
 plt.show()

m()