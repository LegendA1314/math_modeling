import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
krug, = plt.plot([], [], '-', color='g',)

e = 20
plt.axis('equal')
ax.set_xlim(-e, e)
ax.set_ylim(-e, e) 

def circle_big (b, f, t):
    l = f * t * (np.pi / 360) 
    R = l * t
    x = R * np.cos(b)
    y = R * np.sin(b)
    return x, y

def a(i):
    krug.set_data(circle_big(b=np.linspace(0, 2*np.pi, 300), f=1, t=i))

ani = animation.FuncAnimation(fig, a, frames=200, interval=3 )

plt.show()

