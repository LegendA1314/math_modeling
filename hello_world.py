import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d

# Создание пространства для анимации
fig = plt.figure()
ax = plt3d.Axes3D(fig)

# Определение параметров кривой
alpha = np.linspace(0,  np.pi, 100)
beta = np.linspace(0, 2 * np.pi, 100)
x0 = 1
y0 = 1
z0 = 1
R = 5


# Параметрическое задание пространственной кривой
x = R * np.outer(np.cos(alpha), np.sin(beta)) + x0
y = R * np.outer(np.sin(alpha), np.sin(beta)) + y0
z = R * np.outer(np.ones(np.size(alpha)),np.cos(beta)) + z0

# Построение пространственной кривой
ax.plot_surface(x, y, z)

ax.legend()

# Подписи осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Подпись графика
ax.set_title('3D Test')

plt.show()