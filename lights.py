import numpy as np

class Light(object):
    def __init__(self, intensity = 1, color = (1,1,1), lightType = 'None'):
        self.intensity = intensity
        self.color = color
        self.lightType = lightType

    
    def getLightColor(self):
        return [self.color[0] * self.intensity,
                self.color[1] * self.intensity,
                self.color[2] * self.intensity]
    

    def getDiffuseColor(self, intercept):
        return self.getLightColor()


class AmbientLight(Light):
    def __init__(self, intensity=1, color = (1, 1, 1)):
        super().__init__(intensity, color, "Ambient")


class DirectionalLight(Light):
    def __init__(self, direction=(0, -1, 0), intensity=1, color=(1, 1, 1)):
        self.direction = direction / np.linalg.norm(direction)
        super().__init__(intensity, color, "Directional")

    def getDiffuseColor(self, intercept):
        lightColor = super().getDiffuseColor(intercept)

        dir = [i *-1 for i in self.direction]

        intensity = np.dot(intercept.normal, dir) * self.intensity
        intensity = max(0,min(1, intensity))

        diffuseColor = [(i * intensity) for i in self.color]
        return diffuseColor

