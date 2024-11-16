import pygame


class Picture():
    def  __init__(self,put_k_file,size,x,y):
        self.put=put_k_file
        self.size2=size
        self.x=x
        self.y=y
        pict=pygame.image.load(self.put)
        self.object1=pygame.transform.scale(pict,self.size2)
        self.rotated_rock = self.object1
        self.rezult_dergee=15

    def degree_(self):

        uuu=2
        self.rezult_dergee+=uuu
        return self.rezult_dergee

    def draw_debug(self,place:pygame.Surface):
        pygame.draw.rect(place,[0,255,0],[self.x,self.y,self.size2[0],self.size2[1]],1)
        center_X=self.x+self.size2[0]/2
        center_Y=self.y+self.size2[1]/2
        pygame.draw.circle(place,[0,0,222],[center_X,center_Y],2)
        pygame.draw.rect(place,[255,0,0],[center_X-self.rotated_rock.get_width()/2,center_Y-self.rotated_rock.get_height()/2,
                                          self.rotated_rock.get_width(),self.rotated_rock.get_height()],2)

    def draw(self,place:pygame.Surface):
        center_X=self.x+self.size2[0]/2
        center_Y=self.y+self.size2[1]/2
        # place.blit(self.object1,[self.x,self.y])
        place.blit(self.rotated_rock,[center_X-self.rotated_rock.get_width()/2,center_Y-self.rotated_rock.get_height()/2])

    def rotation_def(self):
        self.rotated_rock=pygame.transform.rotate(self.object1,self.degree_())