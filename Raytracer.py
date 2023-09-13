import pygame
from pygame.locals import *
from rt import Raytracer
from figures import *

width = 512
height = 512

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

raytracer = Raytracer(screen)
raytracer.rtClearColor(0.25,0.25,0.25)


raytracer.scene.append(Sphere(position=(0,0,-5), radius = 1))

isRunning = True
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.KEY == pygame.K_ESCAPE:
                isRunning == False
    
    raytracer.rtClear()



    raytracer.rtRender()    
    pygame.display.flip()

pygame.quit()