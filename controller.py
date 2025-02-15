import random

import pygame

import model , bulba,levl
from levl import waves


def cotroller():
    events=pygame.event.get()


    for controller_rock in model.rocks:
        controller_rock.controller(events)

    for bullet2 in model.bullets.copy():
        bullet2.controller(events)

    for event in events:

        if event.type==pygame.KEYDOWN and event.key==pygame.K_d:

            model.moving_ship(5)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            model.moving_ship(-5)

        if event.type==pygame.KEYUP and event.key== pygame.K_SPACE:
            model.line_HP.now_hp=random.randint(5,1000)

        if event.type==pygame.MOUSEBUTTONDOWN and event.button==pygame.BUTTON_LEFT:
            model.new_bullet()

            ###По задумке бульба должна лететь пр нажат на кнопку ЛКМ.###
            ###Есть класс бульба###

        for wave in levl.waves:

            if event.type == wave["номер события таймера"]:
                model.spawn_rock()
                pygame.time.set_timer(move_rock, wave["задержка_меж_камней"])



        if event.type == move_rock:
            model.spawn_rock()

        if event.type==free_type:
            model.moving_ship_2(5)

        if event.type==free_type2:
            model.ship_2.X=-50

        if event.type==pygame.QUIT:
            exit()


def next_level(index):

    first_rock = pygame.event.custom_type()
    dictionary = levl.waves[index]
    dictionary["номер события таймера"]=first_rock
    pygame.time.set_timer(first_rock, dictionary["начаьная_задержка"], 1)




free_type = pygame.event.custom_type()
free_type2 = pygame.event.custom_type()
move_rock=pygame.event.custom_type()

#set_repeat - вкючение ежима зажатия клавиш
pygame.key.set_repeat(10)
pygame.time.set_timer(free_type, 10)
pygame.time.set_timer(free_type2, 10000)


colichstvo_voln=len(levl.waves)
for volna  in range(colichstvo_voln):
    next_level(volna)
print(levl.waves)

