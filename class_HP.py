import pygame,picture
from pygame import Rect
class Hp():
    def __init__(self,x,y,width,height):
        self._x=x
        self.y=y
        self.width=width
        self.height=height
        self.xxx=1000


    def draw_hp(self,place:pygame.Surface):
        a=self.xxx / 1000
        dolay=1-a
        itog=dolay*self.width
        pygame.draw.rect(place,[0,255,0],[self._x,self.y,self.width,self.height])
        pygame.draw.rect(place,[222,0,0],[self._x,self.y,itog,self.height])


