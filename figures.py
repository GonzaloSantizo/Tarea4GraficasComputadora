import numpy as np

class Shape(object):
    def __init__(self, position):
        self.position = position

    def ray_intersect(self, orig, dir):
        return False
    
class Sphere(Shape):
    def __init__(self, position, radius):
        self.radius = radius
        super().__init__(position)

    def ray_intersect(self, orig, dir):
        L = np.subtract(self.position, orig)
        lenghtL = np.linalg.norm(L)
        tca = np.dot(L, dir)

        d = (lenghtL ** 2 - tca ** 2) ** 0.5

        if d > self.radius:
            return False
        return True