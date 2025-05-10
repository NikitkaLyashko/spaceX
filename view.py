
import picture,pygame,process


pygame.init()
wind=pygame.display.set_mode([1500,700])
import model,start_yrovnei

text=pygame.font.SysFont("Arial",50)
cosmos=picture.Picture("sprites/background.jpg", [1500, 700], 0, 0)





list_draw=[    cosmos,
    model.line_HP,
    model.ship_2,
    model.main_ship,
    model.text,
    model.text_2,
    model.game_over]
def view():
    for draw_object in list_draw:
        draw_object.draw(wind)


    pygame.display.set_caption(str(int(model.clock.get_fps())))


    model.wavee.draw(wind)

    for view_bullet in model.bullets:

        view_bullet.draw(wind)



    pygame.display.flip()


