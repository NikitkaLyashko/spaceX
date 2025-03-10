import pygame,picture,messenger
from pygame import Rect
class Hp():
    def __init__(self,x,y,width,height,max_hp,now_hp):

        self._x=x
        self.y=y
        self.width=width
        self.height=height
        self.max_hp=max_hp
        self.now_hp=now_hp


    def HP_line(self):
        global itog
        a = self.now_hp / self.max_hp
        dolay = 1 - a
        itog = dolay * self.width

        if itog >= self.width:
            itog = self.width
            messenger.broadcast("ХП_закончилось", self)


    def draw_hp(self,place:pygame.Surface):
            pygame.draw.rect(place, [0, 255, 0], [self._x, self.y, self.width, self.height])
            pygame.draw.rect(place, [222, 0, 0], [self._x, self.y, itog, self.height])





