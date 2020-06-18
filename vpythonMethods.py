#!/usr/bin/env python
from vpython import *

'''
Aquí usamos vpython, librería para personas mortales y fácil de usar
'''

def cubo():
    print ('Abriendo navegador en localhost ... ')
    box(pos = vector(-2, 2, 0), size = vector(1, 1, 1), color = vector(0, 1, 0))
    box(pos = vector(1, -2, 0),  size = vector(3, 3, 3), color = vector(1, 1, 0))

def esfera():
    print ('Abriendo navegador en localhost ... ')
    sphere(pos = vector(-1, 2, 0), size = vector(1, 1, 1), color = vector(15, 1, 1))
    sphere(pos = vector(1, -2, 0),  size = vector(3, 3, 3), color = vector(5, 10, 1))

def flecha():
    print ('Abriendo navegador en localhost ... ')
    arrow(pos = vector(-2, 0, 0), color = vector(1, 0, 1), axis = vector(1, 2, 2), up = vector(-1, 5, 2))

def cono():
    print ('Abriendo navegador en localhost ... ')
    cone(axis = vector(-1, 4, 0), up = vector(1, 2, 2))

def piramide():
    print ('Abriendo navegador en localhost ... ')
    pyramid(pos = vector(1, -1, 5),  color = vector(0, 1, 0.5))

def cilindro():
    print ('Abriendo navegador en localhost ... ')
    cylinder(axis = vector(-1, 4, 0), up = vector(1, 2, 2))
