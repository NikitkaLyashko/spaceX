import model,picture,pygame
import player
from model import clock, rocks

pygame.init()
text=pygame.font.SysFont("Arial",50)
wind=pygame.display.set_mode([1500,700])
cosmos=picture.Picture("sprites/background.jpg", [1500, 700], 0, 0)






def view():
    cosmos.draw(wind)
    model.ship_2.draw(wind)
    model.main_ship.draw(wind)
    pygame.display.set_caption(str(int(model.clock.get_fps())))
    for rk in model.rocks:
        rk.draw(wind)






    pygame.display.flip()


