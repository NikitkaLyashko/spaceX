import pygame,picture,random

pygame.init()

free_type = pygame.event.custom_type()
pygame.time.set_timer(free_type, 10)

class Rock_space():

    def __init__(self,x,y):
        self._x=x
        self.y=y
        self.x__ = random.randint(-1, 1)
        self.rock=picture.Picture("sprites/Meteorit.png",[50,50],self._x,self.y)


    def draw(self, place: pygame.Surface):
        self.rock.draw(place)
        # self.rock.draw_debug(place)

    def controller(self,events):

        for event in events:

            if event.type == free_type:
                self.rock.y += 2
                self.rock.x+=self.x__
                self.rock.rotation_def()




