import pygame,picture

import messenger

pygame.init()
free_type = pygame.event.custom_type()
pygame.time.set_timer(free_type, 10)
class Bullet():
    def __init__(self,put,size,x,y,rocks):

        self.put=put
        self.size=size
        self._x=x
        self.y=y
        self.rocks=rocks

        self.bulba = picture.Picture(self.put, self.size, self._x, self.y)
        self.rect=pygame.rect.Rect(self._x,self.bulba.y,self.size[0],self.size[1])
        self.draw(pygame.display.get_surface())

    def rect_bullet(self):

        for rect_rocks in self.rocks:
            if self.rect.colliderect(rect_rocks.rect_rock):
                self.rocks.remove(rect_rocks)
                messenger.broadcast("bullet broke rock",self,rect_rocks)


    def draw(self, place: pygame.Surface):
        self.bulba.draw(place)


    def controller(self,events):

        for event in events:

            if event.type == free_type:
                self.bulba.y -= 2
                self.rect.y-=2
                self.rect_bullet()
                # self.bulba.
                # self.bulba.x+=3
                # self.bulba.rotation_def()
