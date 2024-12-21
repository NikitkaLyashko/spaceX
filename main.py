import view,controller,time
from model import clock,rocks

while True:

    # time.sleep(1/60)
    view.view()
    controller.cotroller()
    clock.tick(60)
    print(len(rocks))