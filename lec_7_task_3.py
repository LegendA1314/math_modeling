import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a = float(input())

if a == 1:	
  fig, ax = plt.subplots()
    
  anim_object, = plt.plot([], [], '-', lw=2)

  xdata, ydata = [], []

  ax.set_xlim(-5, 5)
  ax.set_ylim(-5, 5)

  def update(frame): 
    
      xdata.append(np.sin(frame)*(np.exp**np.cos(frame)-2*np.cos(4*frame)+np.sin(frame/12)**5)) 
    
      ydata.append(np.cos(frame)*(np.exp**np.cos(frame)-2*np.cos(4*frame)+np.sin(frame/12)**5)) 
    
      anim_object.set_data(xdata, ydata) 
    
      return anim_object,

  ani = FuncAnimation(fig, update,	frames=np.arange(0, 12*np.pi, 0.1), interval=100)         

    
  ani.save('123.py')

else:	
  fig, ax = plt.subplots()
    
  anim_object, = plt.plot([], [], '-', lw=2)

  xdata, ydata = [], []

  ax.set_xlim(-20, 20)
  ax.set_ylim(-20, 20)

  def update(frame): 
    
      xdata.append(16*np.sin(frame)**3) 
    
      ydata.append(13*np.cos(frame)-5*np.cos(2*frame)-2*cos(3*frame)-np.cos(4*frame)) 
    
      anim_object.set_data(xdata, ydata) 
    
      return anim_object,

  ani = FuncAnimation(fig, update,	frames=np.arange(0, 2*np.pi, 0.1), interval=100)         

    
  ani.save('123.py')

