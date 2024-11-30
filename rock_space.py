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
        self.rect_rock=pygame.rect.Rect(self._x,self.rock.y,50,50)


    def draw(self, place: pygame.Surface):
        self.rock.draw(place)
        pygame.draw.rect(place,[0,0,222],self.rect_rock,1)
        # self.rock.draw_debug(place)



    def controller(self,events):

        for event in events:

            if event.type == free_type:
                self.rock.y += 2
                self.rock.x+=self.x__
                self.rect_rock.y+=2
                self.rect_rock.x+=self.x__
                self.rock.rotation_def()




