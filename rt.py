from math import tan, pi
import numpy as np
from figures import *

class Raytracer(object):
    def __init__(self, screen):
        self.screen = screen
        _,_, self.width, self.height = screen.get_rect()


        self.scene = []
        self.camPosition =  [0,0,0]

        self.rtViewPort(0, 0, self.width, self.height)
        self.rtProyection
        
        self.rtColor(1,1,1)
        self.rtClearColor(0,0,0)
        self.rtClear()


    def rtViewPort(self, posX, posY, width, height):
        self.vpX = posX
        self.vpY = posY
        self.vpWidth  = width
        self.vpHeight = height


    def rtProyection(self, fov = 60, n = 0.1):
        aspectRatio = self.vpWidth / self.vpHeight
        self.nearPlane = n 
        self.topEdge = tan((fov * pi / 180)/2) * self.nearPlane
        self.rightEdge = self.topEdge * aspectRatio


    def rtClearColor(self, r,g,b):
        self.ClearColor = (r * 255,g * 255,b * 255)

    def rtClear(self):
        self.screen.fill(self.ClearColor)
        
    def rtColor(self,r,g,b):
        self.currColor = (r * 255,g * 255,b * 255)


    def rtPoint(self, x,y, color = None):

        y = self.width - y 
        if( 0 <=x < self.width ) and (0 <= y <self.height):
            if color != None:
                color = (color[0] * 255,
                         color[1] * 255,
                         color[2] * 255)
                self.screen.set_at((x,y), color)
            else:
                self.screen.set_at((x,y), self.currColor)

    
    def rtCastRay(self, orig, dir):
        
        for obj in self.scene:
            if obj.ray_intersect(orig, dir):
                return True
        return False


    def rtRender(self):
        for x in range(self.vpX, self.vpX + self.vpWidth + 1):
            for y in range(self.vpY, self.vpY + self.height + 1):
                if 0 <= x < self.width and 0<= y < self.height:
                    Px = ((x + 0.5 - self.vpX) / self.vpWidth) * 2 - 1
                    Py = ((y + 0.5 - self.vpY) / self.vpHeight) * 2 - 1

                    Px *= self.rightEdge
                    Py *= self.topEdge

                    direction = (Px, Py, -self.nearPlane)
                    direction = direction/np.linalg.norm(direction)

                    if self.rtCastRay(self.camPosition, direction):
                        self.rtPoint(x,y)