import random

import pygame.time

import player,class_HP
import rock_space

import second_ship


def moving_ship(x):

    main_ship.X+=x

    # print(main_ship.x)

def moving_ship_2(x):
    ship_2.X+=5
    return 123

def move_rock():
    global next_rock

    next_rock=rock_space.Rock_space(random.randint(30,1500),30)
    rocks.append(next_rock)



main_ship=player.Player("sprites/Enemy.png",[120,120],700,550)
ship_2=second_ship.Second_ship(-50,300)
clock=pygame.time.Clock()
next_rock=rock_space.Rock_space(700,0)
rocks=[next_rock]
line_HP=class_HP.Hp(1170,25,300,50)