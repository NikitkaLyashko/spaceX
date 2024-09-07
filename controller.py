import pygame

import model
import player
import view

free_type = pygame.event.custom_type()

pygame.time.set_timer(free_type, 1000, 0)
print(pygame.MOUSEMOTION)
def cotroller():
    events=pygame.event.get()


    for event in events:

        if event.type==pygame.MOUSEMOTION:
            model.main_ship.draw(view.wind)



        if event.type==pygame.QUIT:
            exit()

