

class Raytracer(object):
    def __init__(self, screen):
        self.screen = screen
        _,_, self.width, self.height = screen.get_rect()

        self.rtColor(1,1,1)
        self.rtClearColor(0.25,0.25,0.25)
        self.rtClear()


    def rtClearColor(self, r,g,b):
        self.ClearColor = (r * 255,g * 255,b * 255)

    def rtClear(self):
        self.screen.fill(self.ClearColor[0])
        
    def rtColor(self,r,g,b):
        self.currColor = (r * 255,g * 255,b * 255)


    def rtPoint(self, x,y, color = None):
        if( 0 <=x < self.width ) and (0 <= y <self.height):
            if color != None:
                color = (color[0] * 255,
                         color[1] * 255,
                         color[2] * 255)
                self.screen.set_at((x,y), color)
            else:
                self.screen.set_at((x,y), self.currColor)


    def rtRender(self):
        pass