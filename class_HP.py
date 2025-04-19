import pygame,picture,messenger,visual_obj,free_process
from pygame import Rect
class Hp(visual_obj.Visual_obj):
    def __init__(self,x,y,width,height,max_hp,now_hp):

        self._x=x
        self.y=y
        self.width=width
        self.height=height
        self.max_hp=max_hp
        self.now_hp=now_hp
        self.HP_line()


    def change_hp(self,hp):
        self.now_hp+=hp
        self.HP_line()


    def HP_line(self):

        a = self.now_hp / self.max_hp
        dolay = 1 - a
        self.itog = dolay * self.width

        if self.itog >= self.width:
            self.itog = self.width
            messenger.broadcast("ХП_закончилось", self)




    def draw(self,place:pygame.Surface):
            pygame.draw.rect(place, [0, 255, 0], [self._x, self.y, self.width, self.height])
            pygame.draw.rect(place, [222, 0, 0], [self._x, self.y, self.itog, self.height])





