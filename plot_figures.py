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

fig.savefig('imgs/non_convex.pdf')

fig = plt.figure(figsize=(16, 10))
ax = fig.gca(projection='3d')

Z = (X**2 + Y**2) / 4
surf = ax.plot_surface(
    X, Y, Z, rstride=1,
    cstride=1, cmap=cm.jet,
    linewidth=0.01)
ax.set_zlim(0, 2)

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
plt.xlabel('$x$')
plt.ylabel('$\sigma(x)$')
plt.grid()
plt.savefig('imgs/non_linear.pdf')


font = {'family' : 'normal',
        'weight' : 'medium',
        'size'   : 10,
       'family': 'sans-serif'}
alpha = {'alpha': 1.0}
matplotlib.rc('font', **font)
matplotlib.rc('grid', **alpha)
N = 1000
x = np.linspace(-10, 10, N)
y = x**2
plt.figure(figsize=(5,5))

start = 15
lr = 0.3
steps = 3

def f(x):
    return x*x

def dx(x):
    return 2*x
theta = start
thetas = []
results = []
thetas.append(theta)
results.append(f(theta))
plt.hold(True)

def plot_line(plt, a, x):
    x1 = np.linspace(x-3, x+3, 2)
    y1 = 2*x*x1 - a
    plt.plot(x1, y1, 'r-')

for s in range(steps):
    theta = theta - lr*dx(theta)
    thetas.append(theta)
    results.append(f(theta))
    plot_line(plt, results[-1], thetas[-1])

plt.plot(x, y)
plt.xlim(-11, 11)
plt.ylim(-10, 100)
plt.xlabel('$x$')
plt.ylabel('$f(x) = x^2$')
plt.grid()
plt.savefig('imgs/gradient_descent.pdf')


img = np.random.randint(0,255,size=(256,256,3))
plt.imshow(img)
plt.savefig('imgs/white_noise.pdf')
