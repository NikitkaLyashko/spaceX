import random


import pygame

import model , bulba,levl

class Text_on_screen():
    def __init__(self,size_window,size):
        self.size_window=size_window

        self.size=size
        self.painter=pygame.font.SysFont("Arial", self.size, True, False)
        self.picture_lev1=self.painter.render("Уровень 1",True,[0,255,0],[0,0,0])



    def draw_text(self,place: pygame.Surface):
        x=self.size_window[0]/2-(self.picture_lev1.get_width()/2)
        y=self.size_window[1]/2-(self.size/2)
        place.blit(self.picture_lev1,[x,y])




