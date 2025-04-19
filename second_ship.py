import pygame,picture,visual_obj

class Second_ship(visual_obj.Visual_obj):
    def __init__(self,x,y):
        self._x=x
        self.y=y
        self.second_ship=picture.Picture("sprites/Skin4.gif",[70,30],self._x,self.y)

    def draw(self, place: pygame.Surface):
        self.second_ship.draw(place)

    @property
    def X(self):
        return  self._x

    @X.setter
    def X(self, x):
        self._x=x
        self.second_ship.x=self._x


