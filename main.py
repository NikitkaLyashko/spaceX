import view,controller,time
from model import clock

while True:

    # time.sleep(1/60)
    view.view()
    controller.cotroller()
    clock.tick(60)
