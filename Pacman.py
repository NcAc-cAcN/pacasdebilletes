import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import os
import numpy as np
import pandas as pd

class Pacman:
    def __init__(self,mapa, mc, x_mc, y_mc):
        #Matriz de control que almacena los IDs de las intersecciones
        self.MC = mc
        #Vectores que almacenan las coordenadas 
        self.XPxToMC = x_mc
        self.YPxToMC = y_mc
        #se resplanda el mapa en terminos de pixeles
        self.mapa = mapa
        self.start = 1
        self.x = 200.0
        self.y = 200.0
        self.speed = 2.0
        self.sprite = 20.0
        
    def loadTextures(self, texturas, id):
        self.texturas = texturas
        self.Id = id
        
    def update(self, dir):
        if dir is None:
            return
        dx, dy = dir[0], dir[1]
        if dx == 0 and dy == 0:
            return
        self.x += dx * self.speed
        self.y += dy * self.speed
        r = self.sprite / 2
        self.x = max(r, min(400 - r, self.x))
        self.y = max(r, min(400 - r, self.y))
                 
    def draw(self):
        glColor3f(1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texturas[self.Id])
        w = self.sprite
        x0 = self.x - w / 2
        y0 = self.y - w / 2
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex2f(x0, y0)
        glTexCoord2f(0.0, 1.0)
        glVertex2f(x0, y0 + w)
        glTexCoord2f(1.0, 1.0)
        glVertex2f(x0 + w, y0 + w)
        glTexCoord2f(1.0, 0.0)
        glVertex2f(x0 + w, y0)
        glEnd()
        glDisable(GL_TEXTURE_2D)