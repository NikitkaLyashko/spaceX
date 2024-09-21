import pygame

import model
import player
import view

free_type = pygame.event.custom_type()

#set_repeat - вкючение ежима зажатия клавиш
pygame.key.set_repeat(10)
pygame.time.set_timer(free_type, 1000, 0)

def cotroller():
    events=pygame.event.get()


    for event in events:

        if event.type==pygame.KEYDOWN and event.key==pygame.K_d:
            print("1111")
            model.moving_ship(5)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            model.moving_ship(-5)




        if event.type==pygame.QUIT:
            exit()

