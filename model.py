import random

import pygame.time,bulba

import messenger
import player,class_HP
import rock_space

import second_ship


def moving_ship(x):
    main_ship.X+=x

def moving_ship_2(x):
    ship_2.X+=5
    return 123

def move_rock():
    global  del_rock_from_model
    next_rock=rock_space.Rock_space(random.randint(30,30),30,50)
    rocks.append(next_rock)
    for del_rock in rocks:

        if del_rock.rock.y >= 700:
            rocks.remove(del_rock)
            del_rock_from_model=1

def new_bullet():
    bulba_object = bulba.Bullet("sprites/bullet.png", [7, 13], main_ship.X + 57, main_ship.Y + 57,rocks)
    bullets.append(bulba_object)


def getter_mess(mess,who,plus_dok):
    global rocks
    if who not in bullets:
        return
    # small_rock1=rock_space.Rock_space(plus_dok.rect_rock.x,plus_dok.rect_rock.y-100,15)
    # small_rock2=rock_space.Rock_space(plus_dok.rect_rock.x,plus_dok.rect_rock.y-100,15)
    # # small_rock3=rock_space.Rock_space(plus_dok.rect_rock.x,plus_dok.rect_rock.y-100,15)
    # rocks.append(small_rock1)
    # rocks.append(small_rock2)
    # rocks.append(small_rock3)
    bullets.remove(who)



messenger.add_sub_def(getter_mess)

main_ship=player.Player("sprites/Enemy.png",[120,120],700,550)
ship_2=second_ship.Second_ship(-50,300)
clock=pygame.time.Clock()
# next_rock=rock_space.Rock_space(700,0)
rocks=[]
bullets=[]
del_rock_from_model=0
line_HP=class_HP.Hp(1170,25,300,50,500,250)
