import class_HP
import model,picture,pygame
import player
from model import clock, rocks

pygame.init()
text=pygame.font.SysFont("Arial",50)
wind=pygame.display.set_mode([1500,700])
cosmos=picture.Picture("sprites/background.jpg", [1500, 700], 0, 0)






def view():
    cosmos.draw(wind)
    model.line_HP.draw_hp(wind)
    model.ship_2.draw(wind)
    model.main_ship.draw(wind)

    pygame.display.set_caption(str(int(model.clock.get_fps())))
    for rock_view in model.rocks:
        rock_view.draw(wind)

    for view_bullet in model.bullets:

        view_bullet.draw(wind)



    pygame.display.flip()


