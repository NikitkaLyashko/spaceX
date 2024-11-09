import random

import pygame

import model
import player
import rock_space
import view
from model import moving_ship_2, move_rock

free_type = pygame.event.custom_type()
free_type2 = pygame.event.custom_type()
free_rock=pygame.event.custom_type()


#set_repeat - вкючение ежима зажатия клавиш
pygame.key.set_repeat(10)
pygame.time.set_timer(free_type, 10)
pygame.time.set_timer(free_type2, 10000)
pygame.time.set_timer(free_rock,500)



def cotroller():
    events=pygame.event.get()


    for controller_rock in model.rocks:
        controller_rock.controller(events)



    for event in events:

        if event.type==pygame.KEYDOWN and event.key==pygame.K_d:
            print("1111")
            model.moving_ship(5)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            model.moving_ship(-5)

        if event.type==pygame.KEYUP and event.key== pygame.K_SPACE:
            model.line_HP.xxx=random.randint(5,1000)
            print(model.line_HP.xxx)
        if event.type==free_rock:
            model.move_rock()

        if event.type==free_type:
            model.moving_ship_2(5)

        if event.type==free_type2:
            model.ship_2.X=-50

        if event.type==pygame.QUIT:
            exit()

