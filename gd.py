import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as plt3d

T = float(input('Температура: '))
M = float(input("Macca: "))
R = float(input("Радиус: "))
omega = float(input("Угол: "))
N = 1000

fig = plt.figure()
ax = plt3d.Axes3D(fig)

fi = np.linspace(0, np.pi, 100)
Q = np.linspace(0, 2 * np.pi, 100)
Msol = 1.9885 * 10 ** 30
Rsol = 6.9551 * 10 ** 8
Msol1 = Msol * 60
Rsol1 = Rsol * 15

if T > 30000 and M > Msol1 and R > Rsol1 :
  x = R * np.outer(np.sin(Q), np.cos(fi))
  y = R * np.outer(np.sin(Q), np.sin(fi))
  z = R * np.outer(np.cos(Q), np.ones(np.size(fi)))

  ball, = ax.plot(x, y, z, 'o', color='b') # Сферический объект
  line, = ax.plot(x, y, z, '-', color='b') # Линия
 

  def animate(i):
    ball.set_data(x[i], y[i])
    ball.set_3d_properties(z[i])
 
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])
 
# Украшательсвта и масштабирование
  ax.set_xlim3d([-1.0, 1.0])
  ax.set_xlabel('X')
 
  ax.set_ylim3d([-1.0, 1.0])
  ax.set_ylabel('Y')
 
  ax.set_zlim3d([-1.0, 1.0])
  ax.set_zlabel('Z')
 
  ani = FuncAnimation(fig, animate, N, interval=50)
 
  ani.save('Класс О.gif')