import pygame,picture,visual_obj


class Player(visual_obj.Visual_obj):
    def __init__(self,put,size,x,y):
        self.put=put
        self.size=size
        self._x=x
        self.y=y

        self.cosmo_ship_for_draw = picture.Picture(self.put, self.size, self._x, self.y)



    def draw(self, place: pygame.Surface):
        self.cosmo_ship_for_draw.draw(place)


    @property
    def X(self):
        return  self._x
    @property
    def Y(self):
        return  self.y


    @X.setter
    def X(self, x):
        self._x=x
        self.cosmo_ship_for_draw.x=self._x


