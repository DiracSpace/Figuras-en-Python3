#!/usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import matplotlib.pyplot as plt
import numpy as np

'''
Aquí usamos librerias de Matplotlib para realizar algunas figuras estáticas
'''

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.grid(True)

class Flecha(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

def esfera():
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_wireframe(x, y, z, color="b")
    ax.set_title('Esfera')
    plt.show()

def cube():
    r = [-1, 1]
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            ax.plot3D(*zip(s, e), color="b")
    ax.set_title('Cubo')
    plt.show()

def flecha():
    ax = plt.axes()
    ax.arrow(0, 0, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
    ax.set_title('Flecha')
    plt.show()

def flecha3D():
    ax.set_xlim([0, 2])
    ax.set_ylim([2, 0])
    ax.set_zlim([0, 2])
    a = Flecha([0, 0.7], [0, 0.5], [1, 1], mutation_scale=25, lw=1.5, arrowstyle="simple", color="b")
    ax.add_artist(a)
    plt.show()

def cono():
    theta = np.linspace(0,2*np.pi,90)
    r = np.linspace(0,3,50)
    T, R = np.meshgrid(theta, r)

    X = R * np.cos(T)
    Y = R * np.sin(T)
    Z = np.sqrt(X**2 + Y**2) - 1

    Z[Z < 0] = np.nan
    Z[Z > 2.1] = np.nan


    ax.plot_wireframe(X, Y, Z)

    ax.set_zlim(0,2)
    plt.show()
