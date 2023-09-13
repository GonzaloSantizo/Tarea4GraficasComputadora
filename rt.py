from math import tan, pi
import numpy as np
from figures import *

class Raytracer(object):
    def __init__(self, screen):
        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()

        self.scene = []
        self.lights = []

        self.camPosition = [0, 0, 0]

        self.rtViewport(0, 0, self.width, self.height)
        self.rtProyection()  # Fixed method call
        
        self.rtColor(1, 1, 1)
        self.rtClearColor(0, 0, 0)
        self.rtClear()

    def rtViewport(self, posX, posY, width, height):  # Corrected method name
        self.vpX = posX
        self.vpY = posY
        self.vpWidth = width
        self.vpHeight = height

    def rtProyection(self, fov=60, n=0.1):
        aspectRatio = self.vpWidth / self.vpHeight
        self.nearPlane = n
        self.topEdge = tan((fov * pi / 180) / 2) * self.nearPlane
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
                color = (int(color[0] * 255),
                         int(color[1] * 255),
                         int(color[2] * 255))
                self.screen.set_at((x,y), color)
            else:
                self.screen.set_at((x,y), self.currColor)

    
    def rtCastRay(self, orig, dir):

        intercept = None
        hit = None
        
        for obj in self.scene:
            intercept = obj.ray_intersect(orig, dir)
            if intercept != None:
                hit = intercept
        return hit


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

                    intercept = self.rtCastRay(self.camPosition, direction)

                    if intercept != None:
                        material = intercept.obj.material

                        colorP = list(material.diffuse)
                        AmbientLight = [0,0,0]
                        DirectionalLight = [0,0,0]

                        for light in self.lights: 
                            if light.lightType == "Ambient":
                                AmbientLight[0] += light.intensity * light.color[0]
                                AmbientLight[1] += light.intensity * light.color[1]
                                AmbientLight[2] += light.intensity * light.color[2]

                            elif light.lightType == "Directional":
                                lightDir = np.array(light.direction) * -1
                                lightDir = lightDir / np.linalg.norm(lightDir)
                                intensity = np.dot(intercept.normal, lightDir)
                                intensity = max(0, min(1, intensity))


                                DirectionalLight[0] += intensity * light.color[0]
                                DirectionalLight[1] += intensity * light.color[1]
                                DirectionalLight[2] += intensity * light.color[2]

                        colorP[0] *= AmbientLight[0] + DirectionalLight[0]
                        colorP[1] *= AmbientLight[1] + DirectionalLight[1]
                        colorP[2] *= AmbientLight[2] + DirectionalLight[2]


                        colorP[0] = min(1, colorP[0])
                        colorP[1] = min(1, colorP[1])
                        colorP[2] = min(1, colorP[2])

                        self.rtPoint(x,y, colorP)

