import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def diff_fumc(s, t):
  x, v_x, y, v_y = s 
  dxdt = v_x
  dvxdt = 0
  dydt = v_y
  dvydt = -1
  return dxdt, dvxdt, dydt, dvydt
  


v = 20
m = 0.5
g= 9.8
alpha = 80 * np.pi / 180
x0 = 3
v_x0 = 0
y0 = -0.08
v_y0 = v * np.sin(alpha)

s0 = x0, v_x0, y0, v_y0


def solve_func(i, key):
    sol = odeint(diff_fumc, s0, t)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')
def animate(i):
  ball.set_data(solve_func(i, 'point'))
  ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 25
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

plt.show()






solve = odeint(diff_fumc, s0, t )
plt.plot(solve[:,0], solve[:,2],  'b', label = 'sdf')
plt.show()