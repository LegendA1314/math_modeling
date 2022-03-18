import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
frames = 200
t = np.linspace(0, 10, frames)

def diff_fumc(s, t):
  y, vy = s 
  dydt = vy
  dvydt = y / (0.008*m)-g
  return dydt,dvydt
  


m =- 0.5
g= 9.8
vy0 = 0.5
y0 =- 0.08
x = np.zeros((len(t)))


s0 = y0, vy0
sol = odeint(diff_fumc, s0, t)


ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
def animate(i):
  ball.set_data(x[i], sol[i, 0])
  ball_line.set_data(x[:i], sol[:i, 0])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=400)

edge = 0.15
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, 0)

plt.show()






# solve = odeint(diff_fumc, s0, t )
# plt.plot(solve[:,0], solve[:,1],  'b', label = 'sdf')
# plt.show()