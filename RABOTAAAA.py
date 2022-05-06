import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d
import imageio
import os

# T = float(input('Температура: '))
# M = float(input("Macca: "))
# R = float(input("Радиус: "))
# omega = float(input("Угол: "))

T = 50000
M = 3e35
R = 7e10
omega = 10
N = 30

fig = plt.figure()
ax = plt3d.Axes3D(fig)

fi = np.linspace(0, np.pi, 100)
Q = np.linspace(0, 2 * np.pi, 100)
Msol = 1.9885 * 10 ** 30
Rsol = 6.9551 * 10 ** 8
Msol1 = Msol * 60
Rsol1 = Rsol * 15

x = R * np.outer(np.sin(Q), np.cos(fi)) 
y = R * np.outer(np.sin(Q), np.sin(fi))
z = R * np.outer(np.cos(Q), np.ones(np.size(fi)))
r = R
key = False

for i in range(N):
  alpha = np.pi / 180 * i * 36
  ax.set_xlim3d([-2*R, 2*R])
  ax.set_xlabel('X')
 
  ax.set_ylim3d([-2*R, 2*R])
  ax.set_ylabel('Y')
 
  ax.set_zlim3d([-2*R, 2*R])
  ax.set_zlabel('Z')

  ax.plot_surface(x, y, z, color='b') 
  plt.savefig(f'pic_{i}')
  
  if r > 2*R or key = True:
    x = x * 0.001
    y = y * 0.001
    z = z * 0.001
    r = r * 0.001
    key = True
  elif r < R:
    x = x * 50
    y = y * 50
    z = z * 50
    r = r * 50
  elif key = False:
    x = x * 1.05
    y = y * 1.05
    z = z * 1.05
    r = r * 1.05

  
images = []
filenames = [f'pic_{i}.png' for i in range(N)] 
for filename in filenames:
  images.append(imageio.imread(filename))
  os.remove(filename)
imageio.mimsave('movie.gif', images)
