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
        self.rect_bulba=pygame.rect.Rect(self._x, self.bulba.y, self.size[0], self.size[1])
        self.draw(pygame.display.get_surface())

    def rect_bullet(self):

        for rock_in_rocks in self.rocks:
            if self.rect_bulba.colliderect(rock_in_rocks.rect_rock):
                self.rocks.remove(rock_in_rocks)
                messenger.broadcast("bullet broke rock", self, rock_in_rocks)

                return 123



    def draw(self, place: pygame.Surface):

        self.bulba.draw(place)


    def controller(self,events):
        for event in events:

            if event.type == free_type:
                self.bulba.y -= 2
                self.rect_bulba.y-=2
                if self.rect_bullet()==123:
                    return
                # self.bulba.
                # self.bulba.x+=3
                # self.bulba.rotation_def()
