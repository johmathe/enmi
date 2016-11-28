from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter

X = np.arange(-2, 2, 0.05)
Y = np.arange(-2, 2, 0.05)
X, Y = np.meshgrid(X, Y)

# Pringle surface
Z = 0.7*np.sin(-X*2*np.cos(Y))
fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_surface(
    X, Y, Z, rstride=2,
    cstride=2, cmap=cm.jet,
    linewidth=0.1)
ax.set_zlim(-1.31, 1.31)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
