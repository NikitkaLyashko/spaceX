import pygame,player

import second_ship


def moving_ship(x):

    main_ship.X+=x

    # print(main_ship.x)

def moving_ship_2(x):
    ship_2.X+=5
    return 123






main_ship=player.Player("sprites/Enemy.png",[120,120],700,550)
ship_2=second_ship.Second_ship(-50,300)

print(moving_ship_2(5))