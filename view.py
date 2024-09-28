import model,picture,pygame
import player

pygame.init()
text=pygame.font.SysFont("Arial",50)
wind=pygame.display.set_mode([1500,700])
cosmos=picture.Picture("sprites/background.jpg", [1500, 700], 0, 0)
metior=picture.Picture("sprites/Meteorit.png",[50,50],700,80)





def view():
    cosmos.draw(wind)
    metior.draw(wind)
    model.ship_2.draw(wind)
    model.main_ship.draw(wind)






    pygame.display.flip()


