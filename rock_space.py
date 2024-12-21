import pygame,picture,random

pygame.init()

free_type = pygame.event.custom_type()
pygame.time.set_timer(free_type, 10)

class Rock_space():

    def __init__(self,x,y,size=50):

        self.size=[size,size]
        self.x__ = random.randint(-10, 10)
        self.x__=self.x__/10
        self.rock=picture.Picture("sprites/Meteorit.png",self.size,x,y)
        self.rect_rock=pygame.rect.Rect(x,y,self.size[0],self.size[1])


    def draw(self, place: pygame.Surface):
        self.rock.draw(place)
        pygame.draw.rect(place,[0,0,222],self.rect_rock,1)
        # self.rock.draw_debug(place)



    def controller(self,events):

        for event in events:

            if event.type == free_type:
                self.rock.y += 1
                # self.rock.x+=self.x__
                self.rect_rock.y+=1
                # self.rect_rock.x=self.rock.x
                self.rock.rotation_def()




