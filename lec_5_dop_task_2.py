import matplotlib.pyplot as plt
import numpy as np

def e(a=4,b=2,p=1,e=0.4):

 X=np.arange(0,6*np.pi,0.1)

 r=p/(1+e*np.cos(X))

 x=r*np.cos(X)
 y=r*np.sin(X)

 plt.plot(x, y, color='b', marker= '>')
 plt.show()

e()

