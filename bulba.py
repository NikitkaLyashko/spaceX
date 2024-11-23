import pygame,picture

class Bullet():
    def __init__(self,put,size,x,y):
        self.put=put
        self.size=size
        self._x=x
        self.y=y

        self.bulba = picture.Picture(self.put, self.size, self._x, self.y)
        self.draw(pygame.display.get_surface())



    def draw(self, place: pygame.Surface):
        self.bulba.draw(place)