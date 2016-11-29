import matplotlib
matplotlib.use('Agg')  # NOQA
from matplotlib import cm
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
rc('text', usetex=True)
alpha = {'alpha': 1.0}
matplotlib.rc('grid', **alpha)


X = np.arange(-2, 2, 0.03)
Y = np.arange(-2, 2, 0.03)
X, Y = np.meshgrid(X, Y)

Z = 0.7 * np.sin(-X * 2 * np.cos(Y))
fig = plt.figure(figsize=(16, 10))
ax = fig.gca(projection='3d')

surf = ax.plot_surface(
    X, Y, Z, rstride=1,
    cstride=1, cmap=cm.jet,
    linewidth=0.01)
ax.set_zlim(-1.31, 1.31)

fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig('imgs/non_convex.pdf')

fig = plt.figure(figsize=(16, 10))
ax = fig.gca(projection='3d')

Z = (X**2 + Y**2) / 4
surf = ax.plot_surface(
    X, Y, Z, rstride=1,
    cstride=1, cmap=cm.jet,
    linewidth=0.01)
ax.set_zlim(0, 2)

fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig('imgs/convex.pdf')


font = {'family': 'normal',
        'weight': 'medium',
        'size': 10, }
alpha = {'alpha': 1.0}
matplotlib.rc('font', **font)
matplotlib.rc('grid', **alpha)


N = 1000
x = np.linspace(-1, 1, N)
x1 = np.zeros(N)
y = np.maximum(x, x1)
plt.figure(figsize=(5,5))
plt.plot(x, y)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.savefig('imgs/non_linear.pdf')
