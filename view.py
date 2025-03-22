
import picture,pygame
pygame.init()
wind=pygame.display.set_mode([1500,700])
import model

text=pygame.font.SysFont("Arial",50)
cosmos=picture.Picture("sprites/background.jpg", [1500, 700], 0, 0)






def view():
    cosmos.draw(wind)
    model.line_HP.draw_hp(wind)
    model.ship_2.draw(wind)
    model.main_ship.draw(wind)
    model.text_object_screen.draw_text(wind)


    pygame.display.set_caption(str(int(model.clock.get_fps())))
    for rock_view in model.rocks:
        rock_view.draw(wind)

    for view_bullet in model.bullets:

        view_bullet.draw(wind)



    pygame.display.flip()


